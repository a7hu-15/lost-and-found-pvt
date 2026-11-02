import pytest
import io
from unittest.mock import MagicMock, patch
from botocore.exceptions import ClientError
from PIL import Image
from fastapi import UploadFile, HTTPException

from app.services.moderation.image_moderator import AmazonRekognitionModerator
from app.services.image_service import process_and_store_image
from app.core.config import settings

def create_test_image_bytes():
    """Generates a simple 100x100 dummy image in memory."""
    buf = io.BytesIO()
    img = Image.new("RGB", (100, 100), color="blue")
    img.save(buf, format="JPEG")
    return buf.getvalue()

@pytest.mark.asyncio
async def test_rekognition_safe_image():
    """Verifies that an image without moderation flags passes moderation."""
    moderator = AmazonRekognitionModerator()
    dummy_bytes = create_test_image_bytes()

    mock_client = MagicMock()
    mock_client.detect_moderation_labels.return_value = {
        "ModerationLabels": []
    }

    with patch.object(settings, "ENABLE_REKOGNITION_MODERATION", True), \
         patch.object(moderator, "_get_client", return_value=mock_client):
        result = await moderator.moderate_image(dummy_bytes)
        assert result.is_safe is True
        assert result.status == "APPROVED"
        assert len(result.flagged_categories) == 0

@pytest.mark.asyncio
async def test_rekognition_rejected_explicit_image():
    """Verifies that an image flagged for Explicit Nudity is rejected."""
    moderator = AmazonRekognitionModerator(confidence_threshold=70.0)
    dummy_bytes = create_test_image_bytes()

    mock_client = MagicMock()
    mock_client.detect_moderation_labels.return_value = {
        "ModerationLabels": [
            {
                "Name": "Explicit Nudity",
                "ParentName": "",
                "Confidence": 94.5
            }
        ]
    }

    with patch.object(settings, "ENABLE_REKOGNITION_MODERATION", True), \
         patch.object(moderator, "_get_client", return_value=mock_client):
        result = await moderator.moderate_image(dummy_bytes)
        assert result.is_safe is False
        assert result.status == "REJECTED"
        assert any("Explicit Nudity" in flag for flag in result.flagged_categories)

@pytest.mark.asyncio
async def test_rekognition_rejected_violence_image():
    """Verifies that an image flagged for Violence is rejected."""
    moderator = AmazonRekognitionModerator(confidence_threshold=70.0)
    dummy_bytes = create_test_image_bytes()

    mock_client = MagicMock()
    mock_client.detect_moderation_labels.return_value = {
        "ModerationLabels": [
            {
                "Name": "Graphic Violence Or Gore",
                "ParentName": "Violence",
                "Confidence": 88.0
            }
        ]
    }

    with patch.object(settings, "ENABLE_REKOGNITION_MODERATION", True), \
         patch.object(moderator, "_get_client", return_value=mock_client):
        result = await moderator.moderate_image(dummy_bytes)
        assert result.is_safe is False
        assert result.status == "REJECTED"

@pytest.mark.asyncio
async def test_rekognition_service_failure_fail_closed():
    """Verifies fail-closed behavior: AWS service failures return status='ERROR'."""
    moderator = AmazonRekognitionModerator()
    dummy_bytes = create_test_image_bytes()

    mock_client = MagicMock()
    mock_client.detect_moderation_labels.side_effect = ClientError(
        {"Error": {"Code": "InternalServerError", "Message": "AWS Rekognition temporary error"}},
        "DetectModerationLabels"
    )

    with patch.object(settings, "ENABLE_REKOGNITION_MODERATION", True), \
         patch.object(moderator, "_get_client", return_value=mock_client):
        result = await moderator.moderate_image(dummy_bytes)
        assert result.is_safe is False
        assert result.status == "ERROR"

@pytest.mark.asyncio
async def test_process_and_store_image_rejects_unsafe_content():
    """Verifies that process_and_store_image raises HTTPException 400 for unsafe images."""
    dummy_bytes = create_test_image_bytes()
    upload = UploadFile(
        filename="unsafe_photo.jpg",
        file=io.BytesIO(dummy_bytes),
        headers={"content-type": "image/jpeg"}
    )

    with patch("app.services.moderation.image_moderator.AmazonRekognitionModerator.moderate_image") as mock_mod:
        from app.services.moderation.image_moderator import ImageModerationResult
        mock_mod.return_value = ImageModerationResult(
            is_safe=False,
            flagged_categories=["Explicit Nudity (95.0%)"],
            labels=[],
            status="REJECTED"
        )
        with pytest.raises(HTTPException) as exc_info:
            await process_and_store_image(upload)
        assert exc_info.value.status_code == 400
        assert "Inappropriate content detected" in exc_info.value.detail

@pytest.mark.asyncio
async def test_process_and_store_image_fail_closed_on_error():
    """Verifies that process_and_store_image raises HTTPException 503 if moderation service is down."""
    dummy_bytes = create_test_image_bytes()
    upload = UploadFile(
        filename="test_photo.jpg",
        file=io.BytesIO(dummy_bytes),
        headers={"content-type": "image/jpeg"}
    )

    with patch("app.services.moderation.image_moderator.AmazonRekognitionModerator.moderate_image") as mock_mod:
        from app.services.moderation.image_moderator import ImageModerationResult
        mock_mod.return_value = ImageModerationResult(
            is_safe=False,
            flagged_categories=["SERVICE_ERROR"],
            labels=[],
            status="ERROR"
        )
        with pytest.raises(HTTPException) as exc_info:
            await process_and_store_image(upload)
        assert exc_info.value.status_code == 503
        assert "Image moderation service is currently unavailable" in exc_info.value.detail
