output "cloudfront_url" {
  description = "The global HTTPS CloudFront URL for the ReFynd platform."
  value       = "https://${aws_cloudfront_distribution.main.domain_name}"
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

