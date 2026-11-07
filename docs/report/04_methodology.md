# CHAPTER 4
# METHODOLOGY AND SYSTEM REQUIREMENTS

---

## 4.1 Software Engineering Methodology (Agile & DevOps)

The development of the ReFynd platform was executed following a tightly integrated **Agile Scrum framework coupled with modern Continuous Engineering / DevOps methodologies**. Because the application combines modern full-stack web technologies with complex distributed cloud infrastructure and automated artificial intelligence pipelines, a traditional linear Waterfall model would have introduced unacceptable risks, delayed testing, and prolonged feedback loops.

```
       +-----------------------------------------------------------+
       |                  Sprint Planning & Backlog                |
       +-----------------------------+-----------------------------+
                                     |
                                     v
       +-----------------------------------------------------------+
       |             Iterative Sprint Development (2 Weeks)        |
       |  - React UI Components (Vite/Tailwind)                    |
       |  - FastAPI Endpoints (Pydantic/Asyncpg)                   |
       |  - Terraform Infrastructure Modules (AWS VPC/ECS/RDS)     |
       +-----------------------------+-----------------------------+
                                     |
                                     v
       +-----------------------------------------------------------+
       |             Continuous Integration (GitHub Actions)       |
       |  - Automated Pytest Suite (18 Unit/Integration Tests)     |
       |  - Flake8 / ESLint Code Quality Gates                     |
       |  - Multi-stage Docker Container Image Compilation         |
       +-----------------------------+-----------------------------+
                                     |
                                     v
       +-----------------------------------------------------------+
       |         Continuous Delivery & Deployment (AWS Cloud)      |
       |  - Amazon ECR Image Publishing (ARM64 Graviton)           |
       |  - Terraform Plan / Apply Infrastructure Execution        |
       |  - ECS Fargate Rolling Deployment & CloudFront Invalidation|
       +-----------------------------+-----------------------------+
                                     |
                                     v
       +-----------------------------------------------------------+
       |             Sprint Review, Telemetry & User Retrospective |
       |  - CloudWatch Logs & Metrics Monitoring                   |
       |  - Performance Latency Benchmarks                         |
       |  - Backlog Refinement for Next Cycle                      |
       +-----------------------------------------------------------+
```
*Figure 4.1: Agile Scrum and DevOps Continuous Engineering Lifecycle*

### Core Engineering Lifecycle Phases:
1. **Requirements Gathering & Sprint Backlog Formulation:**
   User stories were formulated from the perspectives of three core personas: Students (reporters and seekers), Security Attendants (holding desk custodians), and University System Administrators. Each sprint was scoped to a rigorous two-week duration.
2. **Iterative Feature Engineering:**
   Frontend components and backend endpoints were developed concurrently using modular contracts defined via OpenAPI 3.0 schemas.
3. **Automated Quality Assurance Gates:**
   Every code push to GitHub triggered automated continuous integration pipelines via GitHub Actions, executing unit test suites, integration tests, and static linting checks. Merges to the `main` branch required all tests to pass cleanly.
4. **Infrastructure as Code (IaC) Iteration:**
   Cloud infrastructure was version-controlled in the same Git repository alongside application code. Infrastructure modifications were tested through `terraform plan` dry runs before applying to AWS.
5. **Continuous Telemetry and Retrospective:**
   Operational performance metrics—including container memory utilization, API response times, and CloudWatch alarms—were monitored post-deployment to refine subsequent development sprints.

---

## 4.2 Stakeholder and Requirement Analysis

Engineering a campus-wide asset management system requires synthesizing requirements across distinct stakeholder groups with varying technical proficiencies and operational expectations:

* **Primary Stakeholder 1: Campus Students & Faculty (General Users)**
  * *Needs:* Fast reporting without tedious mandatory account signups; ability to quickly check if an item has been found; absolute privacy guarantee for phone numbers and private email addresses; mobile responsiveness.
* **Primary Stakeholder 2: Campus Security Personnel & Desk Custodians**
  * *Needs:* Instant lookup of items deposited at specific holding desks; structured proof-of-ownership verification workflows; protection against false claimant fraud; elimination of physical logbooks.
* **Primary Stakeholder 3: University IT & Campus Administration**
  * *Needs:* Low, predictable cloud infrastructure costs; complete compliance auditability; data protection; prevention of inappropriate or abusive media uploads; zero system downtime.

---

## 4.3 Functional Requirements (FR)

The system enforces twelve core functional requirements governing platform operations:

* **FR-01: Public Item Discovery & Search:**
  The system must provide an accessible, unauthenticated search interface allowing users to query active found items using keywords, categorical filters (e.g., Electronics, Identity Cards, Keys, Books, Clothing), holding desk locations, and date ranges with debounced client-side execution.
* **FR-02: Structured Lost Item Reporting:**
  The system must provide a multi-step guided wizard enabling users to log a lost item with mandatory fields (title, category, date/time lost, last seen location, contact email) and optional private verification details (serial numbers, unique scratches).
* **FR-03: Structured Found Item Reporting:**
  The system must allow finders to record an item by specifying the holding desk or campus custodial location where the item is physically deposited, accompanied by descriptive tags and optional photographic evidence.
* **FR-04: Automated Media Ingestion and Moderation:**
  The system must accept image uploads (JPEG, PNG, WebP up to 10MB), compress and transcode them to WebP format, and submit the bytes to Amazon Rekognition to detect explicit, suggestive, or violent content. Files exceeding a 70% moderation confidence threshold must be rejected with HTTP 400.
* **FR-05: Asymmetric Contact Masking:**
  The public catalog must never expose reporter email addresses, phone numbers, or private verification tokens. Only sanitized item descriptions and custodial desk locations may be publicly visible.
* **FR-06: Cryptographic Token-Based Tracking:**
  Upon report submission, the backend must generate an unguessable tracking token (e.g., `LF-SRM-26-XXXXXX` and a high-entropy secret token) and dispatch a secure private link (`/track?report_id=...&token=...`) to the user’s email address, enabling self-service monitoring and edits.
* **FR-07: Automated Multi-Attribute Item Matching:**
  The backend must execute a similarity scoring engine comparing incoming lost reports against active found reports across category, normalized brand tokens, fuzzy string distances, and location proximity, generating match candidates with confidence percentages.
* **FR-08: Claim Submission Workflow:**
  A student identifying their lost belonging in the found catalog must be able to initiate a formal claim by submitting corroborating private proof of ownership details.
* **FR-09: Administrative Claim Adjudication:**
  Authenticated campus staff must have access to an administrative dashboard to review pending claims, cross-reference claimant descriptions against stored private item information, and transition status to `CLAIMED` or `RESOLVED`.
* **FR-10: Immutable Audit Logging:**
  Every administrative action, status modification, item creation, and claim resolution must generate an immutable record in the `audit_logs` table containing actor ID, IP address, timestamp, action type, and state diff.
* **FR-11: Integrated Support Ticketing:**
  The system must provide an accessible support form allowing users to submit bug reports or inquiries, persisting tickets to PostgreSQL and asynchronously forwarding complete details to the administrative support email.
* **FR-12: Application-Level Rate Limiting:**
  The API gateway must enforce token-bucket rate limits across all routes (10/min for login, 5/min for report creation, 3/min for sensitive actions, 100/min global default), returning HTTP 429 when limits are exceeded.

---

## 4.4 Non-Functional Requirements (NFR)

The architecture is engineered to satisfy rigorous non-functional quality standards:

* **NFR-01: Response Time and Latency:**
  API endpoints must respond within $P_{95} \le 150\text{ ms}$ under normal campus load. Static frontend assets served via CloudFront CDN edge caches must achieve sub-50ms Time-To-First-Byte (TTFB) globally.
* **NFR-02: Availability and Uptime:**
  The production platform must achieve $\ge 99.9\%$ operational uptime, backed by AWS Application Load Balancers, multi-AZ RDS deployment readiness, and ECS Fargate automatic container restart policies.
* **NFR-03: Data Integrity and Consistency (ACID):**
  All database transactions—particularly claim state transitions, report status updates, and audit logging—must strictly adhere to ACID transactional guarantees through PostgreSQL row-level locking.
* **NFR-04: Security and Confidentiality:**
  All network traffic must be encrypted in transit using TLS 1.3 / HTTPS. All database volumes and S3 storage buckets must be encrypted at rest using AES-256 (KMS-managed keys). Passwords must be hashed using Argon2 / Bcrypt with unique salts.
* **NFR-05: Scalability and Elasticity:**
  The containerized compute tier must scale horizontally without architectural refactoring. ECS Fargate task definitions must support scaling from 1 to 10 container replicas based on CPU and memory thresholds.
* **NFR-06: Portability and Cloud Agnosticism:**
  Both frontend and backend must be packaged as standard OCI-compliant Docker containers, ensuring identical execution across local developer workstations (`docker-compose`) and cloud container runtimes.
* **NFR-07: Cost Predictability:**
  Total monthly AWS operational expenses must not exceed \$25.00 during standard collegiate operations, maximizing the utilization of AWS Free Tier allowances and Graviton ARM64 architecture efficiencies.
* **NFR-08: Usability and Accessibility:**
  The frontend user interface must achieve full mobile responsiveness across viewport widths from 360px (smartphones) to 2560px (desktop monitors), following WCAG 2.1 AA accessibility standards for contrast, focus rings, and screen-reader compatibility.
* **NFR-09: Maintainability and Testability:**
  Backend business logic must maintain $\ge 85\%$ test code coverage with automated Pytest execution gates integrated into the GitHub Actions CI pipeline.
* **NFR-10: Resilience and Fail-Closed Safety:**
  External third-party API dependencies (e.g., Amazon Rekognition, Google SMTP) must fail safely. In the event of an AI moderation service outage, media ingestion must fail closed to prevent unmoderated content from entering the platform.

---

## 4.5 Hardware Requirements

The minimum hardware specifications required across development, CI automation, and cloud deployment environments are detailed in Table 4.1.

*Table 4.1: Minimum Hardware Specifications for Development, CI, and Cloud Compute*

| Environment | Processor / Architecture | RAM | Storage / Disk | Network Connectivity |
| :--- | :--- | :--- | :--- | :--- |
| **Developer Workstation** | Apple Silicon M-Series (ARM64) or Intel Core i5/i7 (x86_64) | 16 GB DDR4/Unified | 50 GB SSD (NVMe) | High-Speed Broadband (100 Mbps) |
| **GitHub Actions Runner**| Standard 2-Core Virtual Machine (x86_64) | 7 GB RAM | 14 GB SSD | 1 Gbps Cloud Pipeline |
| **AWS ECS Fargate Task** | AWS Graviton ARM64 (0.25 vCPU) | 512 MB RAM | 20 GB Ephemeral Storage | AWS VPC 10 Gbps Backbone |
| **AWS RDS Database Host**| AWS Graviton ARM64 (`db.t4g.micro`, 2 vCPU) | 1 GB RAM | 20 GB General Purpose SSD (gp3) | Private Subnet VPC Enclave |

---

## 4.6 Software Requirements and Dependency Stack

The platform is constructed using enterprise-grade, open-source software libraries and runtime frameworks, summarized in Table 4.2.

*Table 4.2: Software Stack and Dependency Framework Versions*

| Tier / Component | Technology / Library | Version | Purpose |
| :--- | :--- | :--- | :--- |
| **Frontend Framework** | React | 18.2.0 | Reactive Single-Page Application (SPA) architecture |
| **Language & Typings** | TypeScript | 5.2.2 | Compile-time type safety and interface modeling |
| **Build & Dev Tool** | Vite | 5.0.0 | High-performance bundling and Hot Module Replacement (HMR) |
| **Styling & Design** | Tailwind CSS | 3.3.5 | Utility-first responsive styling and dark mode theme engine |
| **Icons & Visuals** | Lucide React | 0.292.0 | Clean, modern vector iconography |
| **HTTP Client** | Axios / Fetch API | 1.6.0 | RESTful API asynchronous data communication |
| **Backend Runtime** | Python | 3.11.8 | High-throughput asynchronous backend runtime |
| **Backend Framework** | FastAPI | 0.109.0 | High-performance ASGI RESTful microservice framework |
| **ASGI Web Server** | Uvicorn | 0.27.0 | High-concurrency event-loop web server |
| **Data Validation** | Pydantic | 2.6.0 | Strict schema validation, serialization, and typing |
| **Object-Relational Map**| SQLAlchemy (Async) | 2.0.25 | Asynchronous database ORM with AsyncSession |
| **Database Driver** | Asyncpg | 0.29.0 | High-speed native asynchronous PostgreSQL driver |
| **Database Migrations** | Alembic | 1.13.1 | Declarative schema migration and version tracking |
| **Rate Limiting** | SlowAPI / Limits | 0.1.9 | Token-bucket client IP rate-limiting middleware |
| **Image Processing** | Pillow (PIL) | 10.2.0 | In-memory image transcoding, resizing, and WebP compression |
| **Cloud SDK** | Boto3 | 1.34.0 | AWS SDK for Amazon Rekognition and S3 integration |
| **Testing Framework** | Pytest / Pytest-Asyncio | 8.0.0 | Automated unit and asynchronous integration test runner |
| **Infrastructure as Code**| HashiCorp Terraform | 1.7.0+ | Declarative cloud resource provisioning on AWS |

---

## 4.7 Technology Selection Matrix and Justification

Every technology chosen for ReFynd was selected following a comparative trade-off analysis against industry alternatives, detailed in Table 4.3.

*Table 4.3: Technology Selection and Architectural Trade-off Evaluation*

| Architectural Choice | Alternatives Evaluated | Selected Technology | Engineering Justification |
| :--- | :--- | :--- | :--- |
| **Frontend Web Framework** | Vue.js, Angular, Vanilla JS | **React 18 + TypeScript** | Rich component ecosystem, superior virtual DOM reconciliation, compile-time type safety, and massive community library support. |
| **Backend Framework** | Django, Flask, Express.js (Node) | **FastAPI (Python 3.11)** | Native Python async/await concurrency, automatic OpenAPI documentation, 300% faster throughput than Django/Flask, and seamless Python AI/ML integration. |
| **Database Engine** | MongoDB, MySQL, SQLite | **PostgreSQL 16** | Strict ACID compliance, advanced full-text search indexing, native JSONB support, and rock-solid relational foreign-key integrity for audit logs. |
| **Container Compute** | Amazon EC2, AWS EKS (Kubernetes) | **AWS ECS Fargate** | Eliminates server OS patching overhead; zero control-plane fee (saving $73/month vs. EKS); instant native CloudWatch and IAM integration. |
| **Processor Architecture**| x86_64 (Intel / AMD) | **AWS Graviton (ARM64)** | 20% lower cost per vCPU-hour, 40% better price-performance for Python web workloads, and significantly lower carbon footprint. |
| **CDN & Edge Delivery** | Cloudflare, Fastly, Direct S3 | **Amazon CloudFront** | Native integration with AWS S3 and Application Load Balancers, Origin Access Control (OAC), single-pane AWS IAM governance, and free SSL/TLS certificates. |

---

## 4.8 End-to-End Development and Deployment Workflow

The development workflow adheres to a continuous engineering pipeline:
1. **Local Development:** Engineers execute the full stack locally via `docker-compose up`, orchestrating local PostgreSQL, FastAPI backend, and Vite frontend.
2. **Version Control:** Changes are committed to Git feature branches (`feature/xyz`) and submitted via Pull Requests against `main`.
3. **CI Pipeline Validation:** GitHub Actions automatically provisions an isolated Python and Node environment, validates linting, and executes the complete 18-case Pytest test suite.
4. **Container Image Publishing:** Upon successful PR merge, Docker multi-stage images are compiled for ARM64 and pushed to Amazon Elastic Container Registry (ECR).
5. **Infrastructure Deployment:** Terraform executes state reconciliations, provisioning or updating VPC resources, RDS databases, and updating the ECS Fargate task definition revision.
6. **Edge Cache Invalidation:** The deployment pipeline issues an automated cache invalidation (`/*`) across the Amazon CloudFront distribution, ensuring users receive fresh static assets immediately.

---

## 4.9 Project Roles and Responsibilities

To ensure disciplined execution, project responsibilities were mapped across specialized engineering domains, summarized in Table 4.4.

*Table 4.4: Team Roles and Engineering Responsibilities Allocation*

| Engineering Domain | Team Lead / Engineer | Core Technical Responsibilities |
| :--- | :--- | :--- |
| **Cloud Infrastructure & DevOps** | Ashu Chaudhary (Lead) | Terraform IaC modules, AWS VPC networking, ECS Fargate orchestration, CloudFront CDN, ECR, GitHub Actions CI/CD pipelines, CloudWatch alarms. |
| **Backend & AI Architecture** | Backend Engineering Group | FastAPI RESTful route development, SQLAlchemy async ORM, Amazon Rekognition integration, SlowAPI rate limiting, email notification pipelines. |
| **Frontend & UI/UX Engineering** | Frontend Engineering Group | React 18 component development, TypeScript type definitions, Tailwind responsive design, state context, search and tracking dashboards. |
| **Database & Security Governance**| Database Specialist | PostgreSQL schema modeling, foreign key indexing, Alembic migration scripts, Argon2 password hashing, RBAC security, audit logging. |
| **QA & Verification Testing** | Quality Assurance Lead | Pytest unit and integration test authoring, security penetration testing, load testing, bug tracking, and post-mortem documentation. |
