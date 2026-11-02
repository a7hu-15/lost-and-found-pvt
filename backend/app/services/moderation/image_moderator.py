import logging
import asyncio
from typing import List, Tuple, Dict, Any, Optional
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from app.core.config import settings

logger = logging.getLogger(__name__)

# Core moderation categories to strictly reject before image publication
DEFAULT_BLOCKED_CATEGORIES = {
    "Explicit Nudity",
    "Sexual Activity",
    "Graphic Male Nudity",
    "Graphic Female Nudity",
    "Violence",
    "Graphic Violence Or Gore",
    "Visually Disturbing",
    "Hate Symbols",
}

class ImageModerationResult:
    def __init__(self, is_safe: bool, flagged_categories: List[str], labels: List[Dict[str, Any]], status: str):
        self.is_safe = is_safe
        self.flagged_categories = flagged_categories
        self.labels = labels
        self.status = status

    def __repr__(self):
        return f"<ImageModerationResult is_safe={self.is_safe} status={self.status} flags={self.flagged_categories}>"


class AmazonRekognitionModerator:
    """
    AI-powered image moderation service using Amazon Rekognition DetectModerationLabels.
    Inspects image bytes for explicit or inappropriate content before publication.
    """
    def __init__(
        self,
        region_name: str = settings.AWS_REGION,
        confidence_threshold: float = settings.REKOGNITION_CONFIDENCE_THRESHOLD,
        blocked_categories: Optional[set] = None
    ):
        self.region_name = region_name
        self.confidence_threshold = confidence_threshold
        self.blocked_categories = blocked_categories or DEFAULT_BLOCKED_CATEGORIES
        self._client = None

    def _get_client(self):
        if not self._client:
            self._client = boto3.client("rekognition", region_name=self.region_name)
        return self._client

    def _sync_detect(self, image_bytes: bytes) -> List[Dict[str, Any]]:
        client = self._get_client()
        response = client.detect_moderation_labels(
            Image={"Bytes": image_bytes},
            MinConfidence=self.confidence_threshold
        )
        return response.get("ModerationLabels", [])

    async def moderate_image(self, image_bytes: bytes) -> ImageModerationResult:
        """
        Analyzes image bytes against Rekognition moderation labels.
        Fails closed: if Rekognition is enabled and encounters an error, the image is not published.
        """
        if not settings.ENABLE_REKOGNITION_MODERATION:
            logger.info("Rekognition moderation disabled via configuration. Image marked as approved.")
            return ImageModerationResult(
                is_safe=True,
                flagged_categories=[],
                labels=[],
                status="APPROVED"
            )

        loop = asyncio.get_event_loop()
        try:
            labels = await loop.run_in_executor(None, self._sync_detect, image_bytes)
        except (BotoCoreError, ClientError) as aws_err:
            logger.error(f"Amazon Rekognition API call failed: {aws_err}")
            return ImageModerationResult(
                is_safe=False,
                flagged_categories=["SERVICE_ERROR"],
                labels=[],
                status="ERROR"
            )
        except Exception as e:
            logger.error(f"Unexpected error during image moderation: {e}")
            return ImageModerationResult(
                is_safe=False,
                flagged_categories=["UNEXPECTED_ERROR"],
                labels=[],
                status="ERROR"
            )

        flagged_categories = []
        for item in labels:
            name = item.get("Name", "")
            parent = item.get("ParentName", "")
            confidence = item.get("Confidence", 0.0)

            if confidence >= self.confidence_threshold:
                if name in self.blocked_categories or parent in self.blocked_categories:
                    flagged_categories.append(f"{name} ({confidence:.1f}%)")

        if flagged_categories:
            logger.warning(
                f"Image moderation REJECTED: {len(flagged_categories)} flagged category(s) detected: {flagged_categories}"
            )
            return ImageModerationResult(
                is_safe=False,
                flagged_categories=flagged_categories,
                labels=labels,
                status="REJECTED"
            )

        logger.info("Image moderation PASSED: Content verified safe by Amazon Rekognition.")
        return ImageModerationResult(
            is_safe=True,
            flagged_categories=[],
            labels=labels,
            status="APPROVED"
        )


def get_image_moderator() -> AmazonRekognitionModerator:
    return AmazonRekognitionModerator()
