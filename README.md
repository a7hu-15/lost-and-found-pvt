# ReFynd: Campus Lost-and-Found Management Platform

[![CI Pipeline](https://img.shields.io/badge/CI-passing-brightgreen)](https://github.com/a7hu-15/lost-and-found-pvt/actions)
[![AWS Infrastructure](https://img.shields.io/badge/AWS-Fargate%20%7C%20RDS%20%7C%20CloudFront-orange)](https://d25eqjxhksqlbh.cloudfront.net)
[![Terraform](https://img.shields.io/badge/IaC-Terraform-blueviolet)](infra/terraform/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI%200.109-009688)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/Frontend-React%2018%20%7C%20TypeScript-61DAFB)](https://react.dev)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL%2016-336791)](https://www.postgresql.org)
[![License](https://img.shields.io/badge/Academic-B.Tech%20Project-blue)](#license-and-academic-disclaimer)

Live Production URL: https://d25eqjxhksqlbh.cloudfront.net

---

## Production Deployment Links

- Web Application Portal: https://d25eqjxhksqlbh.cloudfront.net
- Public Item Search: https://d25eqjxhksqlbh.cloudfront.net/search
- Report Lost Item: https://d25eqjxhksqlbh.cloudfront.net/report-lost
- Report Found Item: https://d25eqjxhksqlbh.cloudfront.net/report-found
- Private Report Tracking: https://d25eqjxhksqlbh.cloudfront.net/track
- Campus Help and Support: https://d25eqjxhksqlbh.cloudfront.net/support
- Admin and Staff Console: https://d25eqjxhksqlbh.cloudfront.net/admin/login

---

## Overview

ReFynd is a privacy-preserving, cloud-native lost-and-found management platform architected specifically for university campuses and educational institutions. It replaces fragmented paper registers, disorganized physical holding cabinets, and unregulated social media chat groups with an automated, auditable digital clearinghouse.

The platform couples a reactive Single-Page Application (SPA) frontend built with React 18, TypeScript, and Tailwind CSS with an asynchronous RESTful backend built with FastAPI and Python 3.11. The production environment is containerized with Docker, automated with GitHub Actions CI/CD, and fully orchestrated on Amazon Web Services (AWS) using Terraform Infrastructure as Code (IaC).

---

## Key Features

1. Asymmetric Privacy Preservation
   Reporter contact details (email addresses and phone numbers) are encrypted and isolated in private database tables. Public catalog cards display only sanitized item descriptors and physical holding desk locations, eliminating identity leakage and student doxxing.

2. Frictionless Token-Based Tracking
   Users report lost or found items without mandatory upfront account creation. Upon submission, the platform generates a cryptographically unguessable tracking token and delivers a private management URL directly to the user's email inbox.

3. Automated AI Image Moderation
   Uploaded photographs pass through a real-time, fail-closed safety pipeline powered by Amazon Rekognition (DetectModerationLabels). Any media flagged for explicit, suggestive, or inappropriate content with confidence greater than or equal to 70% is rejected immediately before permanent storage.

4. Multi-Attribute Matching Algorithm
   An automated matching engine cross-evaluates incoming lost and found listings across standardized categories, normalized brand tokens, fuzzy string distances (Levenshtein ratios), physical holding desk locations, and temporal proximity windows.

5. Support Ticketing and Real-Time Email Delivery
   Integrated support ticketing captures user inquiries, logs tickets into PostgreSQL, and forwards full details to cloudlostfound.platform@gmail.com with automated confirmation receipts sent to users via Google SMTP over TLS.

6. Application-Level Rate Limiting
   Token-bucket rate limiting enforced via SlowAPI protects endpoints from credential stuffing and automated abuse (10 requests/min for login, 5 requests/min for report creation, 3 requests/min for sensitive actions, 100 requests/min default).

---

## User Workflows

### Reporting a Lost Item
1. The student navigates to the Report Lost page and fills out item details (title, category, date, last seen location, and optional private proof like a serial number).
2. The user provides their contact email and submits the form.
3. The backend generates a unique Report ID (for example, LF-SRM-26-AWX3VM) and an unguessable tracking token.
4. An automated confirmation receipt containing the private tracking link is delivered to the student's email via Google SMTP.
5. The matching engine evaluates the listing against existing found items and flags potential matches.

### Reporting a Found Item
1. A campus finder or staff member navigates to the Report Found page.
2. The finder enters item attributes, specifies the physical campus holding desk (for example, Central Library Reception), and attaches an optional photograph.
3. The image is evaluated in real time by Amazon Rekognition. If safe, it is transcoded to WebP and saved to Amazon S3.
4. The item is published to the public search catalog with its holding desk location so the rightful owner can locate it.

### Verifying and Claiming an Item
1. The rightful owner searches the public catalog and locates their item.
2. The student initiates a claim by providing corroborating private proof of ownership.
3. A security attendant logs into the Admin Console, reviews the claimant's identity and proof against the private record, and approves the release.
4. The item status transitions to CLAIMED and an immutable audit log entry is recorded.

---

## System Architecture

```mermaid
graph TD
    Client([Student / Public Browser]) -->|HTTPS :443 TLS 1.3| CF[Amazon CloudFront CDN<br/>d25eqjxhksqlbh.cloudfront.net]
    
    subgraph AWS Cloud us-east-1
        CF -->|Static SPA Assets /*| S3Static[Amazon S3 Static Bucket<br/>Origin Access Control OAC]
        CF -->|Dynamic API /api/v1/*| ALB[Application Load Balancer<br/>refynd-prod-alb]
        
        subgraph Virtual Private Cloud VPC 10.0.0.0/16
            subgraph Public Subnets
                ALB -->|HTTP :8000| ECS[Amazon ECS Fargate Tasks<br/>ARM64 Graviton Container<br/>FastAPI + Asyncpg]
            end
            
            subgraph Private Subnets
                ECS -->|Port 5432 Encrypted| RDS[(Amazon RDS PostgreSQL 16<br/>db.t4g.micro Private Enclave)]
            end
        end
        
        ECS -->|PutObject / WebP| S3Media[Amazon S3 Uploads Bucket]
        ECS -->|DetectModerationLabels| Rekognition[Amazon Rekognition<br/>AI Image Moderation]
        ECS -->|Logs and Metrics| CloudWatch[Amazon CloudWatch<br/>4 Metric Alarms]
        CloudWatch -->|Alerts| SNS[Amazon SNS Topic<br/>refynd-prod-alerts]
    end
    
    subgraph External Email Network
        ECS -->|SMTP TLS :587| GoogleSMTP[Google SMTP Gateway<br/>cloudlostfound.platform@gmail.com]
        GoogleSMTP -->|Tracking Receipts| UserEmail[Student Inbox]
        GoogleSMTP -->|Support Notifications| AdminEmail[Support Team Inbox]
    end
```

---

## Technology Stack

### Frontend
- Framework: React 18.2 with TypeScript 5.2
- Build Tool: Vite 5.0
- Styling: Tailwind CSS 3.3
- HTTP Client: Axios with normalized API client and request interceptors
- Icons: Lucide React
- Routing: React Router DOM v6 with CloudFront SPA custom error fallbacks

### Backend
- Framework: FastAPI 0.109 (ASGI)
- Language / Runtime: Python 3.11.8
- Web Server: Uvicorn 0.27
- Data Validation: Pydantic v2
- ORM: SQLAlchemy 2.0 (AsyncSession)
- Database Driver: Asyncpg 0.29
- Schema Migrations: Alembic 1.13
- Rate Limiting: SlowAPI 0.1.9 with Upstash Redis adapter support
- Image Processing: Pillow 10.2 (In-memory WebP/JPEG transcoding)
- Cloud SDK: Boto3 1.34

### Database and Infrastructure
- Database: Amazon RDS PostgreSQL 16.2 (Single-AZ, db.t4g.micro, gp3 storage)
- Container Orchestration: Amazon Elastic Container Service (ECS) Fargate
- Compute Architecture: 64-bit ARM64 (AWS Graviton)
- Container Registry: Amazon Elastic Container Registry (ECR)
- Edge CDN: Amazon CloudFront with Origin Access Control (OAC)
- Object Storage: Amazon S3 (Static Frontend and Uploads Buckets)
- AI Moderation: Amazon Rekognition
- Monitoring and Alarms: Amazon CloudWatch and Amazon SNS
- Infrastructure as Code: HashiCorp Terraform 1.7+

---

## Core API Endpoints

| Method | Endpoint | Access Control | Rate Limit | Description |
| :--- | :--- | :--- | :--- | :--- |
| GET | `/health` | Public | None | Container health check probing database reachability |
| GET | `/api/v1/search` | Public | 100/min | Debounced full-text search with category and location filters |
| POST | `/api/v1/lost/create` | Public | 5/min | Registers a lost item and dispatches email tracking receipt |
| POST | `/api/v1/found/create` | Public | 5/min | Ingests found report, moderates image via Rekognition, saves to S3 |
| GET | `/api/v1/track/{report_id}` | Public (Token) | 100/min | Returns private status details when valid tracking token is supplied |
| POST | `/api/v1/claims` | Public | 5/min | Submits ownership proof claiming an available found item |
| POST | `/api/v1/support` | Public | 5/min | Logs support ticket and forwards email to platform administrator |
| POST | `/api/v1/auth/login` | Public | 10/min | Authenticates staff and issues signed JWT Bearer Token |
| GET | `/api/v1/admin/claims` | Staff / Admin | 100/min | Lists pending claims awaiting physical verification |
| POST | `/api/v1/admin/claims/{id}` | Staff / Admin | 10/min | Approves or rejects a claim and updates item status |

---

## Cloud Architecture and Production Operations

### CloudWatch Production Metric Alarms

| Alarm Identifier | Metric Evaluated | Threshold Condition | Evaluation Period | Action Triggered |
| :--- | :--- | :--- | :--- | :--- |
| `refynd-prod-ecs-cpu-high` | Container CPU Utilization | CPU > 80% | 2 Consecutive 1-Min Periods | SNS Alert to Admin Email |
| `refynd-prod-ecs-memory-high` | Container Memory Utilization | Memory > 80% | 2 Consecutive 1-Min Periods | SNS Alert to Admin Email |
| `refynd-prod-alb-5xx-errors` | Load Balancer 5xx Server Errors | Sum > 5 Errors | 5-Minute Window | SNS Alert to Admin Email |
| `refynd-prod-rds-cpu-high` | Database Host CPU Utilization | CPU > 80% | 2 Consecutive 5-Min Periods | SNS Alert to Admin Email |

### Monthly Cloud Cost Optimization Breakdown

| AWS Service | Architecture Strategy | Free Tier Coverage | Est. Monthly Cost |
| :--- | :--- | :--- | :--- |
| Amazon CloudFront | Global edge distribution | 1 TB transfer + 10M requests free/mo | $0.00 |
| Amazon S3 | Static website and uploads | 5 GB standard storage free/mo | ~$0.10 |
| Amazon ECS Fargate | ARM64 Graviton (0.25 vCPU, 0.5 GB RAM) | Pay per second; 20% cheaper than x86 | ~$8.50 |
| Amazon RDS | Single-AZ db.t4g.micro, 20GB gp3 | 750 hours free/mo (first year) | $0.00 (Free Tier) |
| Application Load Balancer | Shared ALB across public subnets | Single ALB handling traffic | ~$12.00 |
| Amazon Rekognition | On-demand moderation with caching | 5,000 images free/mo (first year) | $0.00 |
| Amazon CloudWatch | Centralized logging and alarms | Free tier logging + alarms | ~$0.40 |
| **Total Estimated Cost** | | | **~$21.00 / month** |

### Key Architectural Decisions

1. Serverless Containers over Virtual Machines
   Amazon ECS Fargate eliminates operating system patching, SSH key management, and idle capacity overhead. Compared to Amazon EKS (Kubernetes), Fargate eliminates the $73/month control plane fee while offering native CloudWatch logging and IAM security role binding.

2. AWS Graviton (ARM64) Processors
   Graviton processors deliver 20% lower cost per vCPU-hour and 40% better price-performance compared to fifth-generation x86 processors for containerized Python web workloads.

3. Zero-Trust Relational Database Isolation
   The PostgreSQL database resides strictly in private VPC subnets with no public IP address and no route to the Internet Gateway. The database security group rejects all external connections, permitting traffic solely from the backend ECS task security group on port 5432.

4. Single-Page Application (SPA) Deep-Link Routing
   When React Router routes like `/track` or `/report-lost` are requested directly, Amazon S3 returns a 404 since physical files do not exist at those paths. CloudFront custom error response rules intercept 403 and 404 responses and transparently serve `/index.html` with HTTP 200, enabling React Router to hydrate views without errors.

5. Fail-Closed Computer Vision Moderation
   Uploaded image bytes are evaluated in real time by Amazon Rekognition (DetectModerationLabels). If inappropriate content is detected above a 70% confidence threshold, the file is rejected immediately with an HTTP 400 error. If Rekognition is unreachable, the upload fails closed to protect platform integrity.

---

## Local Development and Containerization

### Prerequisites
- Docker Engine 24.0+ and Docker Compose v2+
- Node.js 20+ and Python 3.11+ (for local non-containerized workflows)

### Running the Complete Stack with Docker Compose
To launch the full multi-tier environment (PostgreSQL 16, FastAPI backend, and React/Nginx frontend) on your local machine:

```bash
docker compose up --build
```

Access points:
- Frontend Application: http://localhost:5173
- Backend API and Swagger Documentation: http://localhost:8000/docs
- Backend Health Probe: http://localhost:8000/health
- PostgreSQL Port: localhost:5433

### Manual Local Setup (Alternative)

#### 1. Backend Setup
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp ../.env.production.example .env
alembic upgrade head
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

#### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

---

## Automated Testing and CI/CD

The project includes an automated test suite executed via Pytest. The tests cover application health probes, Amazon Rekognition fail-closed moderation routines, and support ticket email dispatch pipelines.

### Running Tests Locally
```bash
cd backend
SECRET_KEY=test-secret-key-123456789 PYTHONPATH=. pytest -v
```

### GitHub Actions CI
All commits and pull requests target the `main` branch and trigger the workflow defined in `.github/workflows/ci.yml`. The pipeline installs dependencies, verifies code formatting, and runs all 18 unit and integration test cases.

---

## Cloud Infrastructure Management (Terraform)

All AWS cloud infrastructure is declared in modular Terraform configuration files located in `infra/terraform/`:

```
infra/terraform/
├── main.tf          # Provider configuration and global variables
├── vpc.tf           # VPC, public/private subnets, internet gateways, route tables
├── alb.tf           # Application Load Balancer, listeners, target groups
├── ecs.tf           # ECS Fargate task definitions (ARM64), cluster, services
├── rds.tf           # Amazon RDS PostgreSQL 16 instance and subnet groups
├── s3.tf            # S3 buckets for frontend distribution and media uploads
├── cloudfront.tf    # CloudFront distribution, cache behaviors, OAC, SPA error rules
└── cloudwatch.tf    # CloudWatch log group, 4 metric alarms, SNS alert topic
```

### Applying Infrastructure Updates
```bash
cd infra/terraform
terraform init
terraform plan
terraform apply
```

---

## Directory Structure

```
.
├── README.md                        # Project overview and quickstart
├── docker-compose.yml               # Local multi-service orchestration
├── .env.production.example          # Environment variables template
├── .gitignore                       # Git ignore rules
├── backend/
│   ├── Dockerfile                   # Multi-stage ARM64 Graviton Python container
│   ├── entrypoint.sh                # DB readiness check and migration runner
│   ├── requirements.txt             # Pinned Python dependencies
│   ├── app/
│   │   ├── main.py                  # FastAPI factory and middleware pipeline
│   │   ├── api/v1/                  # RESTful API route controllers
│   │   ├── core/                    # Security, rate limiting, and config settings
│   │   ├── database/                # SQLAlchemy async engine and sessionmaker
│   │   ├── models/                  # Relational database models (PostgreSQL)
│   │   ├── schemas/                 # Pydantic v2 validation models
│   │   └── notifications/           # Asynchronous Google SMTP email service
│   └── tests/                       # Pytest test suites (18 tests passing)
├── frontend/
│   ├── Dockerfile                   # Multi-stage Node/Nginx container
│   ├── nginx.conf                   # Production Nginx reverse proxy configuration
│   ├── package.json                 # Node.js dependencies and scripts
│   └── src/
│       ├── App.tsx                  # Root component and client-side router
│       ├── components/              # Reusable UI components
│       ├── pages/                   # Application views (Search, Track, Report)
│       └── services/                # Axios API client with interceptors
└── infra/
    └── terraform/                   # Production AWS Infrastructure as Code
```

---

## License and Academic Disclaimer

This project was developed for the Bachelor of Technology (B.Tech) degree in Computer Science and Engineering with specialization in Cloud Computing and DevOps at SRM Institute of Science and Technology. All rights reserved.
