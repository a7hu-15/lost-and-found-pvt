# Amazon CloudWatch Log Group for ECS Backend Logs
resource "aws_cloudwatch_log_group" "ecs" {
  name              = "/ecs/${var.app_name}-${var.environment}-backend"
  retention_in_days = 7 # Cost-conscious retention to stay well within CloudWatch free tier (5GB)

  tags = {
    Name = "${var.app_name}-backend-logs"
  }
}

