resource "random_id" "bucket_suffix" {
  byte_length = 4
}

# 1. S3 Bucket for Static Frontend Web Application (React SPA)
resource "aws_s3_bucket" "frontend" {
  bucket        = "${var.app_name}-frontend-${var.environment}-${random_id.bucket_suffix.hex}"
  force_destroy = true

  tags = {
    Name = "${var.app_name}-frontend"
  }
}

resource "aws_s3_bucket_public_access_block" "frontend" {
  bucket = aws_s3_bucket.frontend.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# 2. S3 Bucket for Uploaded Item Images (Moderated via Amazon Rekognition)
resource "aws_s3_bucket" "uploads" {
  bucket        = "${var.app_name}-uploads-${var.environment}-${random_id.bucket_suffix.hex}"
  force_destroy = true

  tags = {
    Name = "${var.app_name}-uploads"
  }
}

resource "aws_s3_bucket_public_access_block" "uploads" {
  bucket = aws_s3_bucket.uploads.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# CORS configuration for uploads bucket
resource "aws_s3_bucket_cors_configuration" "uploads" {
  bucket = aws_s3_bucket.uploads.id

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["GET", "HEAD"]
    allowed_origins = ["*"]
    expose_headers  = ["ETag"]
    max_age_seconds = 3000
  }
}

