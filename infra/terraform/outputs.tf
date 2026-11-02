output "website_url" {
  description = "The S3 Static Website URL for the ReFynd frontend application."
  value       = "http://${aws_s3_bucket_website_configuration.frontend.website_endpoint}"
}

output "https_website_url" {
  description = "The primary secure HTTPS entrypoint for ReFynd."
  value       = "https://${aws_cloudfront_distribution.main.domain_name}"
}

output "cloudfront_domain_name" {
  description = "CloudFront distribution domain name."
  value       = aws_cloudfront_distribution.main.domain_name
}

output "api_url" {
  description = "The Application Load Balancer HTTP endpoint for the FastAPI backend."
  value       = "http://${aws_lb.main.dns_name}"
}

output "alb_dns_name" {
  description = "Application Load Balancer DNS name."
  value       = aws_lb.main.dns_name
}

output "ecr_repository_url" {
  description = "The Amazon ECR Repository URL for pushing backend Docker images."
  value       = aws_ecr_repository.backend.repository_url
}

output "frontend_s3_bucket" {
  description = "The S3 bucket for the React Frontend application."
  value       = aws_s3_bucket.frontend.bucket
}

output "uploads_s3_bucket" {
  description = "The S3 bucket for moderated user uploads."
  value       = aws_s3_bucket.uploads.bucket
}

output "rds_endpoint" {
  description = "The Amazon RDS PostgreSQL instance endpoint."
  value       = aws_db_instance.postgres.endpoint
  sensitive   = true
}

output "ecs_cluster_name" {
  description = "The ECS Cluster name."
  value       = aws_ecs_cluster.main.name
}

output "ecs_service_name" {
  description = "The ECS Service name."
  value       = aws_ecs_service.backend.name
}
