import os
import aiofiles
import asyncio
import logging
from abc import ABC, abstractmethod
from typing import Tuple
import boto3
from app.core.config import settings

logger = logging.getLogger(__name__)

class StorageBackend(ABC):
    @abstractmethod
    async def delete(self, public_url: str):
        pass

    @abstractmethod
    async def save(self, filepath: str, data: bytes) -> Tuple[str, bool, str]:
        """Saves data and returns (public_url, is_flagged, moderation_result)."""
        pass

class LocalStorage(StorageBackend):
    def __init__(self, base_dir: str = "uploads", base_url: str = "/static/uploads"):
        self.base_dir = os.path.join(os.getcwd(), base_dir)
        self.base_url = base_url
        os.makedirs(self.base_dir, exist_ok=True)

    async def delete(self, public_url: str):
        if not public_url or not public_url.startswith(self.base_url):
            return
        rel_path = public_url[len(self.base_url):].lstrip("/")
        full_path = os.path.join(self.base_dir, rel_path)
        if os.path.exists(full_path):
            os.remove(full_path)

    async def save(self, filepath: str, data: bytes) -> Tuple[str, bool, str]:
        full_path = os.path.join(self.base_dir, filepath)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        async with aiofiles.open(full_path, 'wb') as f:
            await f.write(data)
        return f"{self.base_url}/{filepath}", False, "NOT_APPLICABLE"


class S3Storage(StorageBackend):
    """
    Amazon S3 Storage implementation for cloud-native asset storage.
    """
    def __init__(self, bucket_name: str = settings.AWS_S3_BUCKET, region: str = settings.AWS_REGION):
        self.bucket_name = bucket_name
        self.region = region
        self._s3_client = boto3.client("s3", region_name=self.region)

    async def delete(self, public_url: str):
        if not public_url:
            return
        try:
            key = public_url.split(".amazonaws.com/")[-1].lstrip("/")
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, lambda: self._s3_client.delete_object(Bucket=self.bucket_name, Key=key))
        except Exception as e:
            logger.error(f"Failed to delete S3 object {public_url}: {e}")

    async def save(self, filepath: str, data: bytes) -> Tuple[str, bool, str]:
        if not self.bucket_name:
            raise ValueError("AWS_S3_BUCKET is not configured.")
        
        key = f"uploads/{filepath}"
        loop = asyncio.get_event_loop()
        
        def _upload():
            self._s3_client.put_object(
                Bucket=self.bucket_name,
                Key=key,
                Body=data,
                ContentType="image/webp"
            )
            if settings.AWS_CLOUDFRONT_DOMAIN:
                return f"https://{settings.AWS_CLOUDFRONT_DOMAIN}/{key}"
            return f"https://{self.bucket_name}.s3.{self.region}.amazonaws.com/{key}"
        
        public_url = await loop.run_in_executor(None, _upload)
        return public_url, False, "APPROVED"


class CloudinaryStorage(StorageBackend):
    """
    Cloudinary Storage implementation using the official cloudinary package.
    """
    def __init__(self):
        import cloudinary
        import cloudinary.uploader
        cloudinary.config(
            cloud_name=settings.CLOUDINARY_CLOUD_NAME,
            api_key=settings.CLOUDINARY_API_KEY,
            api_secret=settings.CLOUDINARY_API_SECRET,
            secure=True
        )

    async def delete(self, public_url: str):
        if not public_url:
            return
        import cloudinary.uploader
        loop = asyncio.get_event_loop()
        def _del():
            try:
                parts = public_url.split("/")
                public_id = "/".join(parts[-3:]).split(".")[0]
                cloudinary.uploader.destroy(public_id)
            except Exception:
                pass
        await loop.run_in_executor(None, _del)

    async def save(self, filepath: str, data: bytes) -> Tuple[str, bool, str]:
        if not settings.CLOUDINARY_CLOUD_NAME or not settings.CLOUDINARY_API_KEY:
            raise ValueError("Cloudinary credentials not configured")
        import cloudinary.uploader
        loop = asyncio.get_event_loop()
        def _upload():
            try:
                response = cloudinary.uploader.upload(
                    data,
                    public_id=filepath.split('.')[0],
                    resource_type="image",
                    moderation="aws_rek"
                )
                is_flagged = False
                moderation_status = "APPROVED"
                mod_data = response.get("moderation", [])
                if mod_data and isinstance(mod_data, list):
                    status = mod_data[0].get("status", "").lower()
                    if status in ["rejected", "pending"]:
                        is_flagged = True
                        moderation_status = status.upper()
                return response.get("secure_url"), is_flagged, moderation_status
            except Exception as e:
                raise ValueError(f"Cloudinary upload failed: {str(e)}")
        
        return await loop.run_in_executor(None, _upload)


def get_storage_backend() -> StorageBackend:
    if settings.AWS_S3_BUCKET:
        return S3Storage()
    if getattr(settings, "USE_CLOUD_STORAGE", False) and settings.CLOUDINARY_CLOUD_NAME:
        return CloudinaryStorage()
    return LocalStorage()
