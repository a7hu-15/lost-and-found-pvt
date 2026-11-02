# ECS Task Execution Role (used by ECS agent to pull ECR image and write CloudWatch logs)
resource "aws_iam_role" "ecs_execution" {
  name = "${var.app_name}-${var.environment}-ecs-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_execution" {
  role       = aws_iam_role.ecs_execution.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

# ECS Task Role (used by the running FastAPI application itself)
resource "aws_iam_role" "ecs_task" {
  name = "${var.app_name}-${var.environment}-ecs-task-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
      }
    ]
  })
}

# Least-Privilege Policy: Amazon Rekognition Moderation + S3 Uploads
resource "aws_iam_policy" "ecs_app_permissions" {
  name        = "${var.app_name}-${var.environment}-app-policy"
  description = "Allows FastAPI to moderate images with Amazon Rekognition and upload to S3"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "RekognitionImageModeration"
        Effect = "Allow"
        Action = [
          "rekognition:DetectModerationLabels"
        ]
        Resource = "*"
      },
      {
        Sid    = "S3UploadsAccess"
        Effect = "Allow"
        Action = [
          "s3:PutObject",
          "s3:GetObject",
          "s3:DeleteObject"
        ]
        Resource = "${aws_s3_bucket.uploads.arn}/*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_app_permissions" {
  role       = aws_iam_role.ecs_task.name
  policy_arn = aws_iam_policy.ecs_app_permissions.arn
}

