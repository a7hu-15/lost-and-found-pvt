# Generate secure database password if not provided
resource "random_password" "db_password" {
  length  = 20
  special = false # Avoid special characters that might break connection URI strings
}

locals {
  db_password = var.db_password != "" ? var.db_password : random_password.db_password.result
}

# Amazon RDS PostgreSQL Instance (Cost-optimized: db.t4g.micro under AWS Free Tier)
resource "aws_db_instance" "postgres" {
  identifier            = "${var.app_name}-${var.environment}-db"
  engine                = "postgres"
  engine_version        = "16.3"
  instance_class        = "db.t4g.micro"
  allocated_storage     = 20
  max_allocated_storage = 20 # Restricts autoscaling to avoid unexpected storage charges
  storage_type          = "gp3"

  db_name  = var.db_name
  username = var.db_username
  password = local.db_password

  db_subnet_group_name   = aws_db_subnet_group.rds.name
  vpc_security_group_ids = [aws_security_group.rds.id]

  # Security: Private only, strictly unreachable from public internet
  publicly_accessible = false
  skip_final_snapshot = true
  deletion_protection = false

  tags = {
    Name = "${var.app_name}-${var.environment}-db"
  }
}
