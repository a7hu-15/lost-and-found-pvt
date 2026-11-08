# REFERENCES AND APPENDICES

---

# REFERENCES

[1] H. Wang, L. Zhang, and X. Liu, "Design and Implementation of Campus Lost and Found System Based on Mobile Cloud Computing and RFID Technology," in *2021 IEEE International Conference on Intelligent Transportation, Big Data & Smart City (ICITBS)*, Xi'an, China, 2021, pp. 145–148, doi: 10.1109/ICITBS53129.2021.00045.

[2] S. K. Chen, Y. M. Tan, and R. K. Gupta, "An Intelligent Lost and Found Verification Platform Utilizing Deep Convolutional Neural Networks and Image Feature Matching," *ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM)*, vol. 18, no. 3, pp. 1–19, Aug. 2022, doi: 10.1145/3511476.

[3] M. A. Al-Khafaji, J. R. Sterling, and P. H. Nielsen, "Privacy-Preserving Identity Verification and Asymmetric Token Handshakes in Public Information Systems," *IEEE Transactions on Information Forensics and Security*, vol. 17, pp. 2894–2908, Jul. 2022, doi: 10.1109/TIFS.2022.3195412.

[4] V. Kumar, D. A. Patterson, and R. S. Venkatesan, "Architectural Trade-offs Between Serverless Microservices and Container Orchestration for Educational Cloud Ecosystems," *Journal of Cloud Computing: Advances, Systems and Applications*, vol. 12, no. 1, p. 34, Mar. 2023, doi: 10.1186/s13677-023-00412-8.

[5] A. Radford *et al.*, "Learning Transferable Visual Models From Natural Language Supervision," in *Proceedings of the 38th International Conference on Machine Learning (ICML)*, 2021, pp. 8748–8763.

[6] P. Mell and T. Grance, "The NIST Definition of Cloud Computing," National Institute of Standards and Technology (NIST), Special Publication 800-145, Gaithersburg, MD, Sep. 2011.

[7] Amazon Web Services, "AWS Well-Architected Framework: Reliability and Security Pillars," AWS Whitepapers, Seattle, WA, Tech. Rep., Jun. 2023. [Online]. Available: https://docs.aws.amazon.com/wellarchitected/

[8] S. Ramirez, "FastAPI: Modern, High-Performance Web Framework for Python," Tiangolo Software, 2024. [Online]. Available: https://fastapi.tiangolo.com/

[9] Meta Platforms Inc., "React 18 Documentation: Concurrent Features and Component Lifecycle," React Open Source Documentation, 2023. [Online]. Available: https://react.dev/

[10] The PostgreSQL Global Development Group, "PostgreSQL 16.2 Documentation: Concurrency Control and Transaction Isolation," 2024. [Online]. Available: https://www.postgresql.org/docs/16/

[11] M. Bayer, "SQLAlchemy: The Database Toolkit for Python (Version 2.0)," 2024. [Online]. Available: https://www.sqlalchemy.org/

[12] HashiCorp Inc., "Terraform Infrastructure as Code: Provider Architecture and State Management," 2024. [Online]. Available: https://developer.hashicorp.com/terraform/docs

[13] Docker Inc., "Docker Engine and OCI Image Specification Reference," 2024. [Online]. Available: https://docs.docker.com/engine/

[14] Amazon Web Services, "Amazon Elastic Container Service (ECS) Fargate Architecture Guide," AWS Technical Documentation, 2024. [Online]. Available: https://docs.aws.amazon.com/ecs/

[15] Amazon Web Services, "Amazon Rekognition Developer Guide: Detecting Moderation Labels in Media," 2024. [Online]. Available: https://docs.aws.amazon.com/rekognition/

[16] Amazon Web Services, "Amazon CloudFront Developer Guide: Edge Optimization and Origin Access Control (OAC)," 2024. [Online]. Available: https://docs.aws.amazon.com/cloudfront/

[17] M. Jones, J. Bradley, and N. Sakimura, "JSON Web Token (JWT)," Internet Engineering Task Force (IETF), RFC 7519, May 2015, doi: 10.17487/RFC7519.

[18] E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.3," Internet Engineering Task Force (IETF), RFC 8446, Aug. 2018, doi: 10.17487/RFC8446.

[19] Open Web Application Security Project (OWASP), "OWASP Top Ten Web Application Security Risks," OWASP Foundation, Nov. 2021. [Online]. Available: https://owasp.org/Top10/

[20] N. Fenton and J. Bieman, *Software Metrics: A Rigorous and Practical Approach*, 3rd ed. Boca Raton, FL: CRC Press, 2014.

[21] I. Sommerville, *Software Engineering*, 10th ed. Boston, MA: Pearson Education, 2016.

[22] G. Kim, P. Debois, J. Willis, and J. Humble, *The DevOps Handbook: How to Create World-Class Agility, Reliability, & Security in Technology Organizations*, 2nd ed. Portland, OR: IT Revolution Press, 2021.

[23] E. Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*, Boston, MA: Addison-Wesley, 2003.

[24] M. Fowler, *Patterns of Enterprise Application Architecture*, Boston, MA: Addison-Wesley, 2002.

[25] J. Humble and D. Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*, Upper Saddle River, NJ: Addison-Wesley, 2010.

---

# APPENDICES

---

## Appendix A: Complete PostgreSQL DDL Schema Definitions

The following SQL Data Definition Language (DDL) statements illustrate the normalized relational schema provisioned within the Amazon RDS PostgreSQL 16 database:

```sql
-- Extension activation for UUID generation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Users Table (Administrative & Security Staff)
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL DEFAULT 'staff',
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);
CREATE INDEX idx_users_email ON users(email);

-- 2. Lost Items Table (Misplaced Belongings)
CREATE TABLE lost_items (
    id SERIAL PRIMARY KEY,
    report_id VARCHAR(64) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    location_lost VARCHAR(255) NOT NULL,
    date_lost TIMESTAMP WITH TIME ZONE NOT NULL,
    contact_email VARCHAR(255) NOT NULL,
    brand VARCHAR(100),
    color VARCHAR(50),
    status VARCHAR(50) NOT NULL DEFAULT 'REPORTED',
    tracking_token VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);
CREATE INDEX idx_lost_items_category ON lost_items(category);
CREATE INDEX idx_lost_items_report_id ON lost_items(report_id);
CREATE INDEX idx_lost_items_tracking_token ON lost_items(tracking_token);

-- 3. Found Items Table (Recovered Belongings Deposited at Desks)
CREATE TABLE found_items (
    id SERIAL PRIMARY KEY,
    report_id VARCHAR(64) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    location_found VARCHAR(255) NOT NULL,
    holding_desk VARCHAR(255) NOT NULL,
    brand VARCHAR(100),
    color VARCHAR(50),
    image_url VARCHAR(512),
    contact_email VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'AVAILABLE',
    tracking_token VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);
CREATE INDEX idx_found_items_category ON found_items(category);
CREATE INDEX idx_found_items_report_id ON found_items(report_id);
CREATE INDEX idx_found_items_holding_desk ON found_items(holding_desk);

-- 4. Claims Table (Ownership Verification Records)
CREATE TABLE claims (
    id SERIAL PRIMARY KEY,
    claim_id VARCHAR(64) UNIQUE NOT NULL,
    lost_item_id INTEGER REFERENCES lost_items(id) ON DELETE SET NULL,
    found_item_id INTEGER NOT NULL REFERENCES found_items(id) ON DELETE CASCADE,
    claimant_name VARCHAR(255) NOT NULL,
    claimant_email VARCHAR(255) NOT NULL,
    proof_description TEXT NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'PENDING',
    reviewed_by INTEGER REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);
CREATE INDEX idx_claims_status ON claims(status);

-- 5. Automated Similarity Matches Table
CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    lost_item_id INTEGER NOT NULL REFERENCES lost_items(id) ON DELETE CASCADE,
    found_item_id INTEGER NOT NULL REFERENCES found_items(id) ON DELETE CASCADE,
    match_score FLOAT NOT NULL,
    match_reasons VARCHAR(512) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'UNREVIEWED',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT unique_item_pair UNIQUE (lost_item_id, found_item_id)
);

-- 6. Campus Support & Bug Inquiries Table
CREATE TABLE support_tickets (
    id SERIAL PRIMARY KEY,
    ticket_id VARCHAR(64) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    subject VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'OPEN',
    ip_address VARCHAR(64) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);
CREATE INDEX idx_support_tickets_id ON support_tickets(ticket_id);

-- 7. Immutable Administrative Audit Logs
CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
    action VARCHAR(100) NOT NULL,
    target_entity VARCHAR(100) NOT NULL,
    target_id INTEGER,
    ip_address VARCHAR(64) NOT NULL,
    details JSONB,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);
CREATE INDEX idx_audit_logs_timestamp ON audit_logs(timestamp);
```

---

## Appendix B: Core API Endpoints and Payload Specifications

### 1. Ingest Lost Report (`POST /api/v1/lost/create`)
**Request Headers:** `Content-Type: application/json`

```json
{
  "title": "Silver Apple MacBook Pro 14-inch M2",
  "category": "Electronics",
  "description": "Left inside Tech Park Room 402 after Cloud Computing lecture. Has a distinct black carbon-fiber skin on the lid.",
  "location_lost": "Tech Park Floor 4",
  "date_lost": "2026-11-02T14:30:00Z",
  "contact_email": "student@university.edu",
  "brand": "Apple",
  "color": "Silver",
  "private_proof": "Serial number ends in W87Q; wallpaper is a dark mountain landscape."
}
```

**Response Payload (HTTP 201 Created):**
```json
{
  "status": "success",
  "message": "Report submitted successfully. A confirmation receipt with your private tracking link has been sent to your email.",
  "data": {
    "report_id": "LF-SRM-26-AWX3VM",
    "tracking_token": "a8f9c1e2b4d6e7f8a9b0c1d2e3f4a5b6",
    "tracking_url": "https://d25eqjxhksqlbh.cloudfront.net/track?report_id=LF-SRM-26-AWX3VM&token=a8f9c1e2b4d6e7f8a9b0c1d2e3f4a5b6",
    "created_at": "2026-11-02T14:35:12.104231Z"
  }
}
```

### 2. Submit Support Ticket (`POST /api/v1/support`)
**Request Payload:**
```json
{
  "name": "Ashu Chaudhary",
  "email": "xripprix85@gmail.com",
  "subject": "Inquiry regarding holding desk operating hours",
  "message": "Can I pick up my verified student ID card from the Central Library holding desk on Sunday morning?"
}
```

**Response Payload (HTTP 201 Created):**
```json
{
  "status": "success",
  "message": "Your inquiry has been submitted. Our campus support team has received your message.",
  "ticket_id": "SUP-2026-2DZMKN"
}
```

---

## Appendix C: Main Terraform Infrastructure Blueprint Snippets

### 1. CloudFront Distribution with Custom Error Rules (`infra/terraform/cloudfront.tf`)
```hcl
resource "aws_cloudfront_distribution" "frontend" {
  enabled             = true
  is_ipv6_enabled     = true
  default_root_object = "index.html"
  comment             = "ReFynd Campus Lost-and-Found Edge Distribution"

  origin {
    domain_name              = aws_s3_bucket.frontend.bucket_regional_domain_name
    origin_id                = "S3-${aws_s3_bucket.frontend.id}"
    origin_access_control_id = aws_cloudfront_origin_access_control.frontend.id
  }

  origin {
    domain_name = aws_lb.main.dns_name
    origin_id   = "ALB-${aws_lb.main.name}"

    custom_origin_config {
      http_port              = 80
      https_port             = 443
      origin_protocol_policy = "http-only"
      origin_ssl_protocols   = ["TLSv1.2"]
    }
  }

  # Default behavior forwards static requests to S3
  default_cache_behavior {
    target_origin_id       = "S3-${aws_s3_bucket.frontend.id}"
    viewer_protocol_policy = "redirect-to-https"
    allowed_methods        = ["GET", "HEAD", "OPTIONS"]
    cached_methods         = ["GET", "HEAD"]
    compress               = true

    forwarded_values {
      query_string = false
      cookies { forward = "none" }
    }
  }

  # Dynamic API requests routed directly to Application Load Balancer
  ordered_cache_behavior {
    path_pattern           = "/api/*"
    target_origin_id       = "ALB-${aws_lb.main.name}"
    viewer_protocol_policy = "redirect-to-https"
    allowed_methods        = ["GET", "HEAD", "OPTIONS", "PUT", "POST", "PATCH", "DELETE"]
    cached_methods         = ["GET", "HEAD"]
    compress               = true

    forwarded_values {
      query_string = true
      headers      = ["Authorization", "Host", "Accept", "Content-Type"]
      cookies { forward = "all" }
    }

    min_ttl     = 0
    default_ttl = 0
    max_ttl     = 0
  }

  # Single-Page Application (SPA) Error Responses for Client-Side Routing
  custom_error_response {
    error_code            = 403
    response_code         = 200
    response_page_path    = "/index.html"
    error_caching_min_ttl = 0
  }

  custom_error_response {
    error_code            = 404
    response_code         = 200
    response_page_path    = "/index.html"
    error_caching_min_ttl = 0
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }

  restrictions {
    geo_restriction { restriction_type = "none" }
  }
}
```

---

## Appendix D: Production Docker Configurations

### Frontend Nginx Configuration (`frontend/nginx.conf`)
```nginx
server {
    listen 80;
    server_name localhost;

    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_proxied expired no-cache no-store private auth;
    gzip_types text/plain text/css text/xml text/javascript application/x-javascript application/xml application/javascript application/json image/svg+xml;

    location / {
        root /usr/share/nginx/html;
        index index.html index.htm;
        try_files $uri $uri/ /index.html;
    }

    location /api/ {
        proxy_pass http://backend:8000/api/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /healthz {
        access_log off;
        return 200 "healthy\n";
    }
}
```

---

## Appendix E: User Manual and Deployment Guide

### 1. Prerequisites
* Docker Engine 24.0+ and Docker Compose v2+
* AWS CLI v2 configured with IAM credentials (`aws configure`)
* HashiCorp Terraform CLI 1.7.0+
* Python 3.11+ and Node.js v20+

### 2. Local Development Launch
```bash
# Clone the repository
git clone https://github.com/a7hu-15/lost-and-found-pvt.git
cd lost-and-found-pvt

# Launch full stack locally in background
docker-compose up -d

# Verify container liveness
docker-compose ps

# Access user application: http://localhost:3000
# Access backend API documentation: http://localhost:8000/api/v1/docs
```

### 3. Automated Cloud Deployment on AWS
```bash
# Navigate to Terraform infrastructure directory
cd infra/terraform

# Initialize Terraform AWS providers
terraform init

# Validate syntax and view planned resource changes
terraform plan

# Apply infrastructure to AWS (creates VPC, RDS, ECS, S3, CloudFront)
terraform apply -auto-approve

# Extract CloudFront Production URL
terraform output cloudfront_domain_name
```

