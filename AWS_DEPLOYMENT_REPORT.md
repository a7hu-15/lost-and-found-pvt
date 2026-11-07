# ReFynd — Comprehensive AWS Cloud Deployment & Architecture Report

> **Project Name:** ReFynd (Campus Lost-and-Found Web Platform)  
> **Production HTTPS URL:** [https://d25eqjxhksqlbh.cloudfront.net](https://d25eqjxhksqlbh.cloudfront.net)  
> **Admin & Moderation Panel:** [https://d25eqjxhksqlbh.cloudfront.net/admin/login](https://d25eqjxhksqlbh.cloudfront.net/admin/login)  
> **Code Repository:** [https://github.com/a7hu-15/lost-and-found-pvt](https://github.com/a7hu-15/lost-and-found-pvt) (`main` branch)  
> **Target Cloud Provider:** Amazon Web Services (AWS) — Account ID: `757952140199`, Region: `us-east-1`  
> **Report Date:** November 2026  

---

> [!IMPORTANT]
> **Architectural Boundary Note:**
> This report and project infrastructure strictly reflect our dedicated, enterprise AWS cloud architecture (AWS CloudFront, ECS Fargate, RDS PostgreSQL, S3, ALB, Rekognition, CloudWatch, and Terraform IaC). Any external legacy platforms (such as Vercel or third-party serverless wrappers) are strictly omitted and not part of this production system.

---

## 1. Executive Summary & Architecture Blueprint

ReFynd has been transitioned from local development into an automated, highly available, secure, and cost-optimized cloud platform deployed entirely on **Amazon Web Services (AWS)**. The entire infrastructure is provisioned through **Terraform Infrastructure as Code (IaC)**, ensuring repeatability, zero manual console configuration drift, and complete auditability.

```mermaid
graph TD
    User([End User / Student]) -->|HTTPS :443| CF[Amazon CloudFront CDN<br/>d25eqjxhksqlbh.cloudfront.net]
    
    subgraph AWS Cloud us-east-1
        CF -->|Static SPA Assets /*| S3Front[Amazon S3 Bucket<br/>refynd-frontend-prod-a91aeec0]
        CF -->|API Requests /api/*| ALB[Application Load Balancer<br/>refynd-prod-alb]
        
        subgraph VPC 10.0.0.0/16
            subgraph Public Subnets
                ALB -->|Forward :8000| ECS[Amazon ECS Fargate<br/>ARM64 Graviton Container]
            end
            
            subgraph Private Isolated Subnets
                ECS -->|Asyncpg Port 5432| RDS[(Amazon RDS PostgreSQL 16<br/>refynd-prod-db)]
            end
        end
        
        ECS -->|PutObject / WebP| S3Uploads[Amazon S3 Bucket<br/>refynd-uploads-prod-a91aeec0]
        ECS -->|DetectModerationLabels| Rekognition[Amazon Rekognition<br/>AI Image Moderation]
        ECS -->|Metric Alarms & Logs| CloudWatch[Amazon CloudWatch<br/>4 Alarms + Log Group]
        CloudWatch -->|Alerts| SNS[Amazon SNS Topic<br/>refynd-prod-alerts]
    end
    
    subgraph External Secure Services
        ECS -->|SMTP TLS :587| GoogleSMTP[Google SMTP Gateway<br/>cloudlostfound.platform@gmail.com]
        GoogleSMTP -->|Confirmation & Tracking| UserEmail[Student Gmail Inbox]
        GoogleSMTP -->|Support Ticket Forwarding| AdminEmail[Support Team Inbox]
    end
```

---

## 2. Containerization Architecture (Docker & Docker Compose)

The full application is containerized following industry best practices for security, minimal footprint, and reproducibility.

### A. Backend Containerization ([`backend/Dockerfile`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/backend/Dockerfile))
* **Base Image:** `python:3.11-slim` (minimal attack surface, ~150MB base).
* **Security & Privilege Dropping:** Runs as non-root user `appuser` (UID: 1000) to protect against container escape attacks.
* **Health Check:** Native container health check (`curl -f http://localhost:8000/health || exit 1`) with 30s interval, 5s timeout, and 3 retries.
* **Deterministic Entrypoint ([`backend/entrypoint.sh`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/backend/entrypoint.sh)):**
  1. Automated TCP wait-loop verifying PostgreSQL reachability before attempting startup.
  2. Runs database schema migration and initialization (`init_db.py`).
  3. Automatically seeds and verifies the Administrator account (`update_admin.py`).
  4. Launches `uvicorn app.main:app` via `exec` for proper OS signal propagation.
* **Cloud Architecture:** Multi-architecture build (`linux/arm64`) pushed to **Amazon Elastic Container Registry (ECR)**: `757952140199.dkr.ecr.us-east-1.amazonaws.com/refynd-backend:latest`.

### B. Frontend Containerization ([`frontend/Dockerfile`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/frontend/Dockerfile))
* **Multi-Stage Build Pattern:**
  * **Stage 1 (Builder):** `node:20-alpine` compiles TypeScript and Vite production assets (`npm run build`).
  * **Stage 2 (Runtime):** `nginx:1.27-alpine` packages compiled HTML/JS/CSS into a high-performance static server (~25MB total image size).
* **Nginx Configuration ([`frontend/nginx.conf`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/frontend/nginx.conf)):**
  * Gzip compression enabled for CSS, JS, SVG, and JSON.
  * Reverse proxy rules forwarding `/api/*` to the FastAPI backend container.
  * Single Page Application (SPA) fallback handling client-side routes (`try_files $uri $uri/ /index.html;`).
  * Dedicated `/healthz` endpoint returning HTTP 200 for container orchestrators.

### C. Local Orchestration ([`docker-compose.yml`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/docker-compose.yml))
A complete development replica can be launched locally with `docker compose up --build`:
* `refynd-postgres`: PostgreSQL 16 Alpine on port `5433:5432` with Docker health checks.
* `refynd-backend`: FastAPI on port `8000:8000` with dependent health check (`condition: service_healthy`).
* `refynd-frontend`: React/Nginx on port `5173:80`.
* Persistent volumes for database files and local uploads.

---

## 3. Detailed AWS Infrastructure Breakdown

All cloud resources are codified in Terraform under [`infra/terraform/`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/infra/terraform/).

### Phase 1: Virtual Private Cloud (VPC) & Security Groups
* **Network Isolation:** Custom VPC `10.0.0.0/16` configured across two availability zones (`us-east-1a`, `us-east-1b`).
* **Subnets:**
  * 2 Public Subnets: `10.0.1.0/24`, `10.0.2.0/24` (Hosts ALB and ECS tasks).
  * 2 Private Isolated Subnets: `10.0.10.0/24`, `10.0.11.0/24` (Hosts RDS PostgreSQL).
* **Firewall Rules (Least Privilege):**
  * **ALB Security Group (`sg-0ce5ba7d7fbca1378`):** Accepts ingress on HTTP port 80; restricts outbound to ECS tasks only.
  * **ECS Security Group (`sg-023a010dbe3e52f01`):** Ingress permitted ONLY from ALB Security Group on port 8000. No direct internet ingress allowed.
  * **RDS Security Group (`sg-030021aafe59794d7`):** Ingress permitted ONLY from ECS Security Group on port 5432. The database is strictly unreachable from the internet.

### Phase 2: Relational Database Service (Amazon RDS)
* **Engine:** PostgreSQL 16 (`db.t4g.micro`, AWS Graviton2 processor).
* **Storage:** 20 GB gp3 with storage autoscaling enabled.
* **Resilience & Security:**
  * Multi-AZ Subnet Group (`refynd-prod-db-subnet-group`).
  * Automated daily snapshots and performance insights.
  * Connection string injected into ECS via Terraform locals: `postgresql+asyncpg://refynd_admin:***@refynd-prod-db.csn4u66iic9e.us-east-1.rds.amazonaws.com:5432/refynd`.

### Phase 3: Object Storage & Content Moderation
* **Frontend S3 Bucket (`refynd-frontend-prod-a91aeec0`):** Stores static React production assets. Protected via CloudFront Origin Access Control (OAC).
* **Uploads S3 Bucket (`refynd-uploads-prod-a91aeec0`):** Secure storage for student-uploaded item photos.
* **AI Image Moderation (Amazon Rekognition):**
  * Native AWS SDK call to `DetectModerationLabels`.
  * **Fail-Closed Security Architecture:** If moderation encounters an error or timeout, the upload is safely rejected rather than allowed.
  * **Pillow JPEG Transcoder:** Uploaded WebP/PNG images are converted into an in-memory JPEG stream specifically for Rekognition analysis before storing optimized WebP in S3.
  * Blocks suggestive, explicit, or violent imagery with configurable confidence threshold (70.0%).

### Phase 4: Container Orchestration (Amazon ECS Fargate)
* **Cluster:** `refynd-prod-cluster` with Container Insights optimization.
* **Task Definition (`refynd-prod-backend:6`):**
  * **Cost-Optimized Hardware:** AWS Graviton ARM64 architecture, 0.25 vCPU (256 units), 512 MB memory.
  * **IAM Roles:** `ecs_execution_role` (ECR pulling, CloudWatch logging) and `ecs_task_role` (least-privilege S3 and Rekognition access).
* **Application Load Balancer (`refynd-prod-alb`):**
  * Internet-facing ALB with health checks hitting `/health` on 30s intervals.
  * Dynamic target registration across AZs with zero-downtime rolling deployments.

### Phase 5: Automated CI/CD Pipeline (GitHub Actions)
* **Workflow ([`.github/workflows/ci.yml`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/.github/workflows/ci.yml)):**
  1. Triggers on every push to `main` branch.
  2. Sets up Python 3.11, PostgreSQL, and installs dependencies.
  3. Executes test suite: **18 automated pytest cases** covering health checks, Rekognition moderation, email validation, and support routing.
  4. Authenticates to AWS via GitHub Secrets (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`).
  5. Builds multi-stage ARM64 Docker images and pushes to Amazon ECR.
  6. Updates the ECS Fargate service for zero-downtime rolling deployments.

### Phase 6: Global CDN & SSL/TLS Termination (Amazon CloudFront)
* **Distribution ID:** `E2D6HFDGFXT0R5`
* **Secured HTTPS Domain:** `https://d25eqjxhksqlbh.cloudfront.net`
* **Single-Domain Unified Routing:**
  * `/api/*` -> Forwarded dynamically to the Application Load Balancer with zero cache (`CachingDisabled`) and full header forwarding.
  * `/*` -> Served from Amazon S3 with Origin Access Control (OAC) and gzip/brotli edge compression.
  * **Custom Error Handling:** HTTP 403 and 404 responses from S3 are mapped to `/index.html` with HTTP 200 to guarantee seamless React client-side routing.
* **Security:** AWS managed TLS certificate with enforced HTTP-to-HTTPS automatic redirection (valid green padlock in all browsers).

### Phase 7: Live Email Delivery & Customer Support System
* **Confirmation Receipt Dispatch:**
  * When a user logs a lost or found report, a background task queues `send_report_confirmation_email`.
  * The email provides the unique **Report ID** (e.g. `LF-SRM-26-CSVSQM`), the item name, and a direct **"Track Your Report"** button resolving to the secure CloudFront URL:
    ```
    https://d25eqjxhksqlbh.cloudfront.net/track?report_id={report_id}&token={access_token}
    ```
* **Customer Support & Issue Reporting:**
  * When any user submits a message via the **"Need Help? / Contact Support"** page, the system stores the ticket in RDS (`SUP-2026-***`) and automatically dispatches the complete ticket details (name, email, subject, message, IP, timestamp) to:
    ```
    cloudlostfound.platform@gmail.com
    ```
  * An automated acknowledgment receipt is simultaneously sent to the submitter's email address.
  * Background execution via FastAPI `BackgroundTasks` ensures instant, zero-latency response (`201 Created`).
* **Authenticated SMTP Gateway:** Google SMTP over TLS (`smtp.gmail.com:587`) configured with authenticated credentials via Terraform IaC.

### Phase 8: Observability, Metrics & Alerting (Amazon CloudWatch)
* **Log Group:** `/ecs/refynd-prod-backend` collecting real-time stdout/stderr from backend containers.
* **4 Metric Alarms (Terraform Managed):**
  1. `refynd-prod-ecs-cpu-high`: Triggers if ECS Backend CPU exceeds 80% for 2 periods.
  2. `refynd-prod-ecs-memory-high`: Triggers if ECS Backend Memory exceeds 80% for 2 periods.
  3. `refynd-prod-alb-5xx-errors`: Triggers if ALB 5xx server errors exceed 5 within 5 minutes.
  4. `refynd-prod-rds-cpu-high`: Triggers if PostgreSQL database CPU exceeds 80% for 2 periods.
* **Alerting SNS Topic:** `refynd-prod-alerts` wired to send instant email alerts to administrators upon threshold breaches.

---

## 4. Current Status & Verification Table

| Component | Technology | AWS Resource Name / Identifier | Production Status |
| :--- | :--- | :--- | :--- |
| **Web Portal** | React 18 + CloudFront CDN | `https://d25eqjxhksqlbh.cloudfront.net` | Live & Secured (HTTPS) |
| **API Gateway / ALB** | AWS Application Load Balancer | `refynd-prod-alb-1704449525.us-east-1.elb.amazonaws.com` | Healthy (2 Targets Active) |
| **Backend Compute** | AWS ECS Fargate (ARM64) | `refynd-prod-cluster` / `refynd-prod-service` (Task Rev: 6) | Running & Auto-healing |
| **Database** | Amazon RDS PostgreSQL 16 | `refynd-prod-db` (`db.t4g.micro`, 20GB gp3) | Healthy & Encrypted |
| **Static Hosting S3** | Amazon S3 + OAC | `refynd-frontend-prod-a91aeec0` | Active |
| **Uploads S3** | Amazon S3 + CORS | `refynd-uploads-prod-a91aeec0` | Active |
| **AI Moderation** | Amazon Rekognition | `DetectModerationLabels` (Fail-closed) | Active |
| **Container Registry** | Amazon ECR | `757952140199.dkr.ecr.us-east-1.amazonaws.com/refynd-backend` | Active |
| **Email Delivery** | Google SMTP via TLS | `cloudlostfound.platform@gmail.com` (:587) | Verified & Dispatching |
| **Monitoring & Alarms** | Amazon CloudWatch + SNS | `/ecs/refynd-prod-backend` + 4 Metric Alarms | Active & Monitoring |
| **CI/CD Pipeline** | GitHub Actions | `.github/workflows/ci.yml` | Passing (18/18 Tests Green) |

---

## 5. Cost Optimization & Budget Breakdown

To minimize cloud costs for college and academic operations while maintaining production-grade reliability, the architecture implements several key optimizations:

| Service | Architecture Strategy | Free Tier Coverage | Est. Monthly Cost |
| :--- | :--- | :--- | :--- |
| **Amazon CloudFront** | Global edge distribution | 1 TB data transfer + 10M requests free/mo | **$0.00** |
| **Amazon S3** | Static website & image uploads | 5 GB standard storage free/mo | **~$0.10** |
| **Amazon ECS Fargate** | ARM64 Graviton (0.25 vCPU, 0.5 GB RAM) | 20% cheaper than x86; pay per second | **~$8.50** |
| **Amazon RDS** | Single-AZ `db.t4g.micro`, 20GB gp3 | 750 hours free/mo (1st year) | **$0.00** (Free Tier) |
| **Application Load Balancer**| Shared ALB across public subnets | Single ALB handling traffic | **~$12.00** |
| **Amazon Rekognition** | On-demand moderation with caching | 5,000 images free/mo (1st year) | **$0.00** |
| **Amazon CloudWatch** | 5GB logs free, container insights disabled | Free tier logging + alarms | **~$0.40** |
| **Total Predicted Monthly Cost** | | | **~$21.00 / month** |

---

## 6. Viva Defense & Architecture Q&A (Academic Readiness)

### Q1: Why did you choose Amazon ECS Fargate instead of EC2 or Kubernetes?
> **Answer:** ECS Fargate is serverless container orchestration. Unlike EC2, we do not need to patch the underlying Linux OS, manage SSH keys, or pay for idle capacity. Compared to EKS (Kubernetes), Fargate eliminates the $73/month control plane fee while offering native CloudWatch logging and IAM security role binding.

### Q2: Why use ARM64 Graviton instead of x86?
> **Answer:** AWS Graviton processors are built on ARM64 architecture, providing 20% lower cost per vCPU-hour and 40% better price-performance compared to fifth-generation x86 processors for containerized Python web workloads.

### Q3: How is user data kept secure in the database?
> **Answer:** The PostgreSQL database resides strictly in private VPC subnets with no public IP address and no route to the Internet Gateway. The database security group rejects all external connections, permitting traffic solely from the backend ECS task security group on port 5432. All contact details are obfuscated, and access tokens are hashed.

### Q4: How does the application handle single-page routing without 404s?
> **Answer:** When React Router routes like `/track` or `/report-lost` are requested, Amazon S3 returns a 404 since the physical file does not exist. Our CloudFront distribution intercepts 403 and 404 responses and transparently serves `/index.html` with HTTP 200, enabling React Router to hydrate the view seamlessly.

### Q5: What happens if an image containing inappropriate content is uploaded?
> **Answer:** Uploaded image bytes are transcoded to JPEG in memory and sent to Amazon Rekognition `DetectModerationLabels`. If explicit or suggestive content is detected above a 70% confidence threshold, the file is rejected immediately with an HTTP 400 error and is never saved to S3. If Rekognition is unavailable, the pipeline fails closed to prevent unmoderated content from entering the platform.
