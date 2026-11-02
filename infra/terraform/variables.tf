variable "aws_region" {
  description = "The AWS region to deploy infrastructure into."
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment identifier (e.g. prod, staging, dev)."
  type        = string
  default     = "prod"
}

variable "app_name" {
  description = "Name of the application."
  type        = string
  default     = "refynd"
}

variable "db_name" {
  description = "Name of the PostgreSQL database."
  type        = string
  default     = "refynd"
}

variable "db_username" {
  description = "Master username for PostgreSQL database."
  type        = string
  default     = "refynd_admin"
}

variable "db_password" {
  description = "Master password for PostgreSQL database (if blank, will be randomly generated)."
  type        = string
  sensitive   = true
  default     = ""
}

variable "jwt_secret_key" {
  description = "Secret key used for JWT signing."
  type        = string
  sensitive   = true
  default     = ""
}

variable "admin_email" {
  description = "Initial Administrator email."
  type        = string
  default     = "cloudlostfound.admin@gmail.com"
}

variable "admin_password" {
  description = "Initial Administrator password."
  type        = string
  sensitive   = true
  default     = "Bheda15@"
}

variable "backend_image" {
  description = "Docker image URI for the backend container in ECR."
  type        = string
  default     = ""
}

variable "smtp_user" {
  description = "SMTP username for email dispatch (e.g. cloudlostfound.platform@gmail.com)."
  type        = string
  default     = "cloudlostfound.platform@gmail.com"
}

variable "smtp_password" {
  description = "Google App Password (16 characters) for SMTP dispatch."
  type        = string
  sensitive   = true
  default     = ""
}

