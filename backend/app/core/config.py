import os
from typing import List, Union
from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "ReFynd Platform"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    MATCH_THRESHOLD: float = 80.0
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", f"https://{os.getenv('VERCEL_PROJECT_PRODUCTION_URL', os.getenv('VERCEL_URL'))}" if os.getenv("VERCEL_URL") or os.getenv("VERCEL_PROJECT_PRODUCTION_URL") else "http://localhost:5173")
    
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    
    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "sqlite+aiosqlite:///./lost_found.db"
    )

    @validator("DATABASE_URL", pre=True)
    def fix_database_url(cls, v: str) -> str:
        if v and v.startswith("postgresql://"):
            v = v.replace("postgresql://", "postgresql+asyncpg://", 1)
        if v and "sslmode=require" in v:
            v = v.replace("sslmode=require", "ssl=require")
        return v
    
    # Upstash Redis
    UPSTASH_REDIS_REST_URL: str = os.getenv("UPSTASH_REDIS_REST_URL", "")
    UPSTASH_REDIS_REST_TOKEN: str = os.getenv("UPSTASH_REDIS_REST_TOKEN", "")
    
    # CORS
    BACKEND_CORS_ORIGINS: Union[List[str], str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:8080",
        "http://127.0.0.1:5173",
    ]
    
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str):
            if v.startswith("[") and v.endswith("]"):
                import json
                try:
                    return json.loads(v)
                except Exception:
                    pass
            return [i.strip() for i in v.split(",") if i.strip()]
        elif isinstance(v, list):
            return v
        return []
    
    # Cloudinary Storage Configuration
    CLOUDINARY_CLOUD_NAME: str = os.getenv("CLOUDINARY_CLOUD_NAME", "")
    CLOUDINARY_API_KEY: str = os.getenv("CLOUDINARY_API_KEY", "")
    CLOUDINARY_API_SECRET: str = os.getenv("CLOUDINARY_API_SECRET", "")

    # AWS Storage & AI Moderation Configuration
    AWS_REGION: str = os.getenv("AWS_REGION", "us-east-1")
    AWS_S3_BUCKET: str = os.getenv("AWS_S3_BUCKET", "")
    AWS_CLOUDFRONT_DOMAIN: str = os.getenv("AWS_CLOUDFRONT_DOMAIN", "")
    ENABLE_REKOGNITION_MODERATION: bool = os.getenv("ENABLE_REKOGNITION_MODERATION", "false").lower() == "true"
    REKOGNITION_CONFIDENCE_THRESHOLD: float = float(os.getenv("REKOGNITION_CONFIDENCE_THRESHOLD", "70.0"))

    # Storage
    USE_CLOUD_STORAGE: bool = os.getenv("USE_CLOUD_STORAGE", "True" if os.getenv("CLOUDINARY_CLOUD_NAME") or os.getenv("AWS_S3_BUCKET") else "False").lower() == "true"
    UPLOAD_DIR: str = "uploads"  # used when USE_CLOUD_STORAGE=False
    # SMTP Configuration
    SUPPORT_EMAIL: str = "cloudlostfound.platform@gmail.com"
    SMTP_HOST: str = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", 587))
    SMTP_USER: str = os.getenv("SMTP_USER", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")
    SMTP_FROM: str = os.getenv("SMTP_FROM", "ReFynd <cloudlostfound.platform@gmail.com>")
    MOCK_SMTP: bool = False

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()
