resource "random_password" "jwt_secret" {
  length  = 32
  special = false
}

locals {
  jwt_secret    = var.jwt_secret_key != "" ? var.jwt_secret_key : random_password.jwt_secret.result
  backend_image = var.backend_image != "" ? var.backend_image : "${aws_ecr_repository.backend.repository_url}:latest"
}

# ECS Cluster
resource "aws_ecs_cluster" "main" {
  name = "${var.app_name}-${var.environment}-cluster"

  setting {
    name  = "containerInsights"
    value = "disabled" # Keep disabled to avoid CloudWatch custom metric charges
  }

  tags = {
    Name = "${var.app_name}-cluster"
  }
}

# ECS Fargate Task Definition (Cost-optimized: 0.25 vCPU, 0.5 GB RAM)
resource "aws_ecs_task_definition" "backend" {
  family                   = "${var.app_name}-${var.environment}-backend"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  execution_role_arn       = aws_iam_role.ecs_execution.arn
  task_role_arn            = aws_iam_role.ecs_task.arn

  container_definitions = jsonencode([
    {
      name      = "backend"
      image     = local.backend_image
      essential = true

      portMappings = [
        {
          containerPort = 8000
          hostPort      = 8000
          protocol      = "tcp"
        }
      ]

      environment = [
        {
          name  = "DATABASE_URL"
          value = "postgresql+asyncpg://${var.db_username}:${local.db_password}@${aws_db_instance.postgres.endpoint}/${var.db_name}"
        },
        {
          name  = "SECRET_KEY"
          value = local.jwt_secret
        },
        {
          name  = "ENABLE_REKOGNITION_MODERATION"
          value = "true"
        },
        {
          name  = "REKOGNITION_CONFIDENCE_THRESHOLD"
          value = "70.0"
        },
        {
          name  = "AWS_REGION"
          value = var.aws_region
        },
        {
          name  = "AWS_S3_BUCKET"
          value = aws_s3_bucket.uploads.bucket
        },
        {
          name  = "AWS_CLOUDFRONT_DOMAIN"
          value = aws_cloudfront_distribution.main.domain_name
        },
        {
          name  = "MOCK_SMTP"
          value = "True"
        },
        {
          name  = "FRONTEND_URL"
          value = "https://${aws_cloudfront_distribution.main.domain_name}"
        }
      ]

      logConfiguration = {
        logDriver = "awslogs"
        options = {
          "awslogs-group"         = aws_cloudwatch_log_group.ecs.name
          "awslogs-region"        = var.aws_region
          "awslogs-stream-prefix" = "backend"
        }
      }
    }
  ])

  tags = {
    Name = "${var.app_name}-task-def"
  }
}

# ECS Fargate Service
resource "aws_ecs_service" "backend" {
  name            = "${var.app_name}-${var.environment}-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.backend.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [aws_subnet.public_1.id, aws_subnet.public_2.id]
    security_groups  = [aws_security_group.ecs.id]
    assign_public_ip = true # Direct Internet egress via IGW ($0 NAT Gateway cost)
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.backend.arn
    container_name   = "backend"
    container_port   = 8000
  }

  depends_on = [
    aws_lb_listener.http,
    aws_db_instance.postgres
  ]

  tags = {
    Name = "${var.app_name}-service"
  }
}
