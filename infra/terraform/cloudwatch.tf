# Amazon CloudWatch Log Group for ECS Backend Logs
resource "aws_cloudwatch_log_group" "ecs" {
  name              = "/ecs/${var.app_name}-${var.environment}-backend"
  retention_in_days = 7 # Cost-conscious retention to stay well within CloudWatch free tier (5GB)

  tags = {
    Name = "${var.app_name}-backend-logs"
  }
}

# SNS Topic for CloudWatch Metric Alarms
resource "aws_sns_topic" "alerts" {
  name = "${var.app_name}-${var.environment}-alerts"

  tags = {
    Name = "${var.app_name}-alerts"
  }
}

# CloudWatch Alarm: ECS CPU Utilization > 80%
resource "aws_cloudwatch_metric_alarm" "ecs_cpu_high" {
  alarm_name          = "${var.app_name}-${var.environment}-ecs-cpu-high"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "CPUUtilization"
  namespace           = "AWS/ECS"
  period              = 300
  statistic           = "Average"
  threshold           = 80
  alarm_description   = "Triggers when ECS backend CPU utilization exceeds 80% for two consecutive 5-minute periods"
  alarm_actions       = [aws_sns_topic.alerts.arn]

  dimensions = {
    ClusterName = aws_ecs_cluster.main.name
    ServiceName = aws_ecs_service.backend.name
  }

  tags = {
    Name = "${var.app_name}-ecs-cpu-alarm"
  }
}

# CloudWatch Alarm: ECS Memory Utilization > 80%
resource "aws_cloudwatch_metric_alarm" "ecs_memory_high" {
  alarm_name          = "${var.app_name}-${var.environment}-ecs-memory-high"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "MemoryUtilization"
  namespace           = "AWS/ECS"
  period              = 300
  statistic           = "Average"
  threshold           = 80
  alarm_description   = "Triggers when ECS backend memory utilization exceeds 80% for two consecutive 5-minute periods"
  alarm_actions       = [aws_sns_topic.alerts.arn]

  dimensions = {
    ClusterName = aws_ecs_cluster.main.name
    ServiceName = aws_ecs_service.backend.name
  }

  tags = {
    Name = "${var.app_name}-ecs-memory-alarm"
  }
}

# CloudWatch Alarm: ALB 5XX Target Errors > 5
resource "aws_cloudwatch_metric_alarm" "alb_5xx_high" {
  alarm_name          = "${var.app_name}-${var.environment}-alb-5xx-errors"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "HTTPCode_Target_5XX_Count"
  namespace           = "AWS/ApplicationELB"
  period              = 300
  statistic           = "Sum"
  threshold           = 5
  alarm_description   = "Triggers when the Application Load Balancer detects more than 5 server 5xx errors in 5 minutes"
  alarm_actions       = [aws_sns_topic.alerts.arn]

  dimensions = {
    LoadBalancer = aws_lb.main.arn_suffix
  }

  tags = {
    Name = "${var.app_name}-alb-5xx-alarm"
  }
}

# CloudWatch Alarm: RDS PostgreSQL CPU Utilization > 80%
resource "aws_cloudwatch_metric_alarm" "rds_cpu_high" {
  alarm_name          = "${var.app_name}-${var.environment}-rds-cpu-high"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "CPUUtilization"
  namespace           = "AWS/RDS"
  period              = 300
  statistic           = "Average"
  threshold           = 80
  alarm_description   = "Triggers when RDS PostgreSQL CPU utilization exceeds 80% for two consecutive 5-minute periods"
  alarm_actions       = [aws_sns_topic.alerts.arn]

  dimensions = {
    DBInstanceIdentifier = aws_db_instance.postgres.identifier
  }

  tags = {
    Name = "${var.app_name}-rds-cpu-alarm"
  }
}
