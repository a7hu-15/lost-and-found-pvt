import os
import uuid
from datetime import datetime
import io
import logging
from PIL import Image, ImageOps
from fastapi import UploadFile, HTTPException

logger = logging.getLogger(__name__)

UPLOAD_DIR = os.path.join(os.getcwd(), "uploads")
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

async def process_and_store_image(file: UploadFile):
    if not file:
        return None, None, False, None

    ALLOWED_MIMES = {"image/jpeg", "image/png", "image/webp"}
    if file.content_type not in ALLOWED_MIMES:
        raise HTTPException(
            status_code=400,
            detail="Invalid MIME type. Only JPEG, PNG, and WebP are allowed."
        )

    # Check extension
    ext = os.path.splitext(file.filename)[1].lower() if file.filename else ""
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Invalid image format. Only JPG, PNG, and WebP are allowed."
        )

    # Read bytes and check size
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="Image size exceeds 10 MB limit."
        )

    now = datetime.utcnow()

    # Unique filenames
    file_id = uuid.uuid4().hex
    main_filename = f"{file_id}.webp"
    thumb_filename = f"{file_id}_thumb.webp"

    try:
        # Open with PIL
        file.file.seek(0)
        img = Image.open(file.file)

        # Transpose image based on EXIF orientation and STRIP all EXIF metadata (GPS, device info)
        img = ImageOps.exif_transpose(img)
        
        # Convert RGBA / P palette to RGB for WebP compatibility
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # 1. Main image: Max 1200px
        main_img = img.copy()
        main_img.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
        
        main_buffer = io.BytesIO()
        main_img.save(main_buffer, "WEBP", quality=82, optimize=True)
        main_bytes = main_buffer.getvalue()

        # 2. Thumbnail: Max 300px
        thumb_img = img.copy()
        thumb_img.thumbnail((300, 300), Image.Resampling.LANCZOS)
        
        thumb_buffer = io.BytesIO()
        thumb_img.save(thumb_buffer, "WEBP", quality=75, optimize=True)
        thumb_bytes = thumb_buffer.getvalue()

    except Exception as e:
        logger.error(f"Failed to process and transcode image: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Failed to process image: {str(e)}")

    # 3. Content Moderation: Amazon Rekognition DetectModerationLabels
    # Inspects image bytes before storing or associating with any public listing
    from app.services.moderation.image_moderator import get_image_moderator
    moderator = get_image_moderator()
    mod_result = await moderator.moderate_image(main_bytes)

    if mod_result.status == "ERROR":
        # Fail closed: Do not publish or persist image if moderation service fails
        logger.error("Rejecting image upload because moderation service encountered an error.")
        raise HTTPException(
            status_code=503,
            detail="Image moderation service is currently unavailable. Please try again or submit your report without an image."
        )

    if not mod_result.is_safe:
        # Image contains prohibited content - reject before storage
        reasons_str = ", ".join(mod_result.flagged_categories)
        logger.warning(f"Image rejected during pre-upload moderation: {reasons_str}")
        raise HTTPException(
            status_code=400,
            detail=f"Image upload rejected: Inappropriate content detected ({reasons_str})."
        )

    # 4. Storage: Persist only approved images
    from app.services.storage import get_storage_backend
    storage = get_storage_backend()

    main_url, _, _ = await storage.save(f"{now.year}/{now.month:02d}/{main_filename}", main_bytes)
    thumb_url, _, _ = await storage.save(f"{now.year}/{now.month:02d}/{thumb_filename}", thumb_bytes)

    return main_url, thumb_url, False, "APPROVED"


async def delete_image(public_url: str):
    from app.services.storage import get_storage_backend
    storage = get_storage_backend()
    await storage.delete(public_url)
