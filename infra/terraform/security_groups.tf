# Security Group for Application Load Balancer
resource "aws_security_group" "alb" {
  name        = "${var.app_name}-${var.environment}-alb-sg"
  description = "Allows inbound HTTP/HTTPS traffic to Application Load Balancer"
  vpc_id      = aws_vpc.main.id

  ingress {
    description = "HTTP from Internet"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTPS from Internet"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Forward to ECS tasks"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.app_name}-${var.environment}-alb-sg"
  }
}

# Security Group for ECS Fargate Containers
resource "aws_security_group" "ecs" {
  name        = "${var.app_name}-${var.environment}-ecs-sg"
  description = "Allows inbound traffic to ECS ONLY from the Application Load Balancer"
  vpc_id      = aws_vpc.main.id

  ingress {
    description     = "Inbound from ALB on port 8000"
    from_port       = 8000
    to_port         = 8000
    protocol        = "tcp"
    security_groups = [aws_security_group.alb.id]
  }

  egress {
    description = "Outbound to Internet (for Rekognition API, S3 uploads, ECR pull)"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.app_name}-${var.environment}-ecs-sg"
  }
}

# Security Group for Amazon RDS PostgreSQL
resource "aws_security_group" "rds" {
  name        = "${var.app_name}-${var.environment}-rds-sg"
  description = "Strictly isolates RDS: allows inbound PostgreSQL connections ONLY from ECS tasks"
  vpc_id      = aws_vpc.main.id

  ingress {
    description     = "PostgreSQL from ECS tasks only"
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.ecs.id]
  }

  tags = {
    Name = "${var.app_name}-${var.environment}-rds-sg"
  }
}

