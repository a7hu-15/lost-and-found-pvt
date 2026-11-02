# CloudFront Origin Access Control for Frontend Bucket
resource "aws_cloudfront_origin_access_control" "frontend_oac" {
  name                              = "${var.app_name}-frontend-oac"
  description                       = "OAC for ReFynd Frontend S3 Bucket"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

# CloudFront Origin Access Control for Uploads Bucket
resource "aws_cloudfront_origin_access_control" "uploads_oac" {
  name                              = "${var.app_name}-uploads-oac"
  description                       = "OAC for ReFynd Uploads S3 Bucket"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

# CloudFront Distribution: Single Entrypoint for SPA, API, and Static Uploads
resource "aws_cloudfront_distribution" "main" {
  enabled             = true
  is_ipv6_enabled     = true
  comment             = "ReFynd Global CDN"
  default_root_object = "index.html"
  price_class         = "PriceClass_100" # 1TB data transfer free per month permanently

  # Origin 1: React Static Frontend (S3)
  origin {
    domain_name              = aws_s3_bucket.frontend.bucket_regional_domain_name
    origin_id                = "S3-Frontend"
    origin_access_control_id = aws_cloudfront_origin_access_control.frontend_oac.id
  }

  # Origin 2: FastAPI Backend (ALB)
  origin {
    domain_name = aws_lb.main.dns_name
    origin_id   = "ALB-Backend"

    custom_origin_config {
      http_port              = 80
      https_port             = 443
      origin_protocol_policy = "http-only" # ALB HTTP listener
      origin_ssl_protocols   = ["TLSv1.2"]
    }
  }

  # Origin 3: Moderated Item Images (S3)
  origin {
    domain_name              = aws_s3_bucket.uploads.bucket_regional_domain_name
    origin_id                = "S3-Uploads"
    origin_access_control_id = aws_cloudfront_origin_access_control.uploads_oac.id
  }

  # Default Cache Behavior: Frontend Single Page Application
  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD", "OPTIONS"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-Frontend"

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 86400
    max_ttl                = 31536000
    compress               = true
  }

  # Ordered Behavior: /api/* -> Route directly to Backend ALB
  ordered_cache_behavior {
    path_pattern     = "/api/*"
    allowed_methods  = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "ALB-Backend"

    forwarded_values {
      query_string = true
      headers      = ["Authorization", "Host", "Accept", "Content-Type", "Origin"]
      cookies {
        forward = "all"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 0
    max_ttl                = 0
    compress               = true
  }

  # Ordered Behavior: /uploads/* -> Route to S3 Uploads Bucket
  ordered_cache_behavior {
    path_pattern     = "/uploads/*"
    allowed_methods  = ["GET", "HEAD"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-Uploads"

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 86400
    max_ttl                = 31536000
    compress               = true
  }

  # Single Page Application (SPA) Error Redirection for React Router
  custom_error_response {
    error_code         = 403
    response_code      = 200
    response_page_path = "/index.html"
  }

  custom_error_response {
    error_code         = 404
    response_code      = 200
    response_page_path = "/index.html"
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true # Free SSL/TLS certificate (*.cloudfront.net)
  }

  tags = {
    Name = "${var.app_name}-cdn"
  }
}
