# A PROJECT REPORT ON
# ReFynd: A Scalable, Privacy-Preserving, and Cloud-Native Lost-and-Found Management Platform for Educational Campuses

---

### Submitted in partial fulfillment of the requirements for the award of the degree of
## BACHELOR OF TECHNOLOGY
### in
### COMPUTER SCIENCE AND ENGINEERING
**(Specialization in Cloud Computing and DevOps)**

---

**Submitted by:**
* **Ashu Chaudhary** (Reg. No: RA2211003010xxx)
* **Undergraduate Project Team**

**Under the Guidance of:**
* **Project Supervisor / Faculty Guide**
* Department of Computer Science and Engineering
* SRM Institute of Science and Technology, Kattankulathur, Chennai, India

---

<br/>

```
                DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING
               FACULTY OF ENGINEERING AND TECHNOLOGY
           SRM INSTITUTE OF SCIENCE AND TECHNOLOGY
           Kattankulathur, Chengalpattu District, Tamil Nadu – 603203
                              NOVEMBER 2026
```

\newpage

---

## BONAFIDE CERTIFICATE

Certified that this project report titled **"ReFynd: A Scalable, Privacy-Preserving, and Cloud-Native Lost-and-Found Management Platform for Educational Campuses"** is the bonafide work of **Ashu Chaudhary (Reg. No: RA2211003010xxx)** and team members, who carried out the project work under my supervision during the academic year 2025–2026 in partial fulfillment of the requirements for the award of the degree of **Bachelor of Technology in Computer Science and Engineering (Cloud Computing and DevOps)**.

<br/><br/><br/>

___________________________                             ___________________________
**Project Guide / Supervisor**                         **Head of the Department**
Department of Computer Science & Engg.                 Department of Computer Science & Engg.
SRM Institute of Science and Technology                SRM Institute of Science and Technology
Kattankulathur - 603203                                Kattankulathur - 603203

<br/><br/>

Submitted for the University Project Viva-Voce Examination held on: _____________________

<br/><br/>

___________________________                             ___________________________
**Internal Examiner**                                   **External Examiner**

\newpage

---

## DECLARATION

We hereby declare that the project work entitled **"ReFynd: A Scalable, Privacy-Preserving, and Cloud-Native Lost-and-Found Management Platform for Educational Campuses"** submitted to the Department of Computer Science and Engineering, SRM Institute of Science and Technology, Kattankulathur, Chennai, is a record of original engineering work done by us under the supervision and guidance of our project guide.

We further declare that this report has not previously formed the basis for the award of any Degree, Diploma, Associateship, Fellowship, or any other similar title to any candidate of any University or Institution. All ideas, architectures, models, and quotes borrowed from existing literature and documentation have been duly cited and acknowledged in accordance with standard academic and IEEE referencing conventions.

<br/><br/><br/>

**Place:** Kattankulathur, Chennai  
**Date:** November 2026  

<br/>

**Ashu Chaudhary**  
*(Register No: RA2211003010xxx)*  
Department of Computer Science and Engineering  
SRM Institute of Science and Technology  

\newpage

---

## ACKNOWLEDGEMENT

The satisfaction that accompanies the successful completion of any task would be incomplete without the mention of people whose ceaseless cooperation made it possible, whose constant guidance and encouragement served as a beacon of light and crowned our efforts with success.

First and foremost, we express our profound gratitude to **SRM Institute of Science and Technology** for providing us with state-of-the-art computational infrastructure, cloud access, and academic resources necessary to execute this project successfully.

We express our sincere thanks and deep sense of gratitude to our respected **Head of the Department**, Department of Computer Science and Engineering, for their valuable support, administrative encouragement, and for providing a highly conducive academic environment.

We take immense pride and pleasure in expressing our deep and heartfelt gratitude to our **Project Supervisor and Faculty Guide**, for their invaluable guidance, constructive criticism, inspiring discussions, and sustained interest throughout the course of this project. Their profound insights into distributed cloud computing, DevOps automation, and secure web architectures have helped us elevate this project from a conceptual idea into a production-grade enterprise deployment.

We also convey our sincere thanks to all the faculty members, technical laboratory assistants, and staff members of the Department of Computer Science and Engineering for their direct and indirect assistance at various stages of our work.

Finally, we owe our deepest gratitude to our beloved **parents and family members** for their endless patience, moral support, and blessings, and to our **friends and peers** for their continuous camaraderie and intellectual feedback during the development, testing, and documentation of this work.

<br/><br/>

**Ashu Chaudhary & Team**

\newpage

---

## ABSTRACT

In modern academic institutions and university campuses characterized by large student populations and sprawling physical infrastructure, the loss and recovery of personal belongings—such as laptops, identification credentials, keys, electronics, and academic materials—represent a significant daily logistical challenge. Traditional campus lost-and-found management relies heavily on fragmented, antiquated processes: physical paper registers stationed across disparate security desks, unorganized noticeboards, and ad-hoc, informal instant messaging groups (e.g., WhatsApp and Telegram). These legacy mechanisms suffer from severe information asymmetry, total absence of real-time searchability, lack of claim verification, complete exposure of sensitive personally identifiable information (PII), and high administrative overhead for campus security personnel.

To address these systemic deficiencies, this project presents **ReFynd**, an enterprise-grade, privacy-preserving, and cloud-native lost-and-found management platform architected specifically for collegiate ecosystems. ReFynd introduces a structured three-tier reactive web architecture comprising a high-performance modern frontend built with **React 18, TypeScript, and Tailwind CSS**, an asynchronous high-throughput backend powered by **FastAPI and Python 3.11**, and an ACID-compliant transactional persistence layer utilizing **PostgreSQL 16 via SQLAlchemy and Alembic**. 

Key engineering innovations in ReFynd include:
1. **Automated Asymmetric Privacy Protection:** Sensitive personal details (phone numbers, physical addresses, personal email addresses) are permanently encrypted and sequestered from public interfaces; listings present only non-sensitive descriptive attributes and sanitized holding desk locations.
2. **Cryptographic Self-Service Tracking:** Users submit reports without mandatory upfront account creation, receiving a cryptographically generated Report ID and secure tracking token that grants authorized access to private management dashboards and status updates.
3. **AI-Powered Image Moderation:** User-uploaded media passes through an asynchronous content validation pipeline integrated with **Amazon Rekognition** (`DetectModerationLabels`), executing fail-closed safety checks that intercept explicit, offensive, or hazardous uploads before persistent S3 commit.
4. **Automated Matching Engine:** A multi-factor similarity algorithm cross-evaluates categorical tags, normalized brand/model identifiers, fuzzy text tokens, physical holding desk locations, and temporal proximity windows to automatically generate match scores and alert owners.
5. **Full Cloud and DevOps Automation:** The entire platform has been containerized using multi-stage **Docker** architectures (optimized for 64-bit ARM Graviton compute) and orchestrated locally via **Docker Compose**. The production environment is provisioned entirely via **Terraform Infrastructure as Code (IaC)** on **Amazon Web Services (AWS)** across a secure Virtual Private Cloud (VPC) featuring Amazon CloudFront CDN edge caching, Application Load Balancers (ALB), Amazon Elastic Container Service (ECS) Fargate serverless containers, Amazon Relational Database Service (RDS), Amazon S3 Object Storage with Origin Access Control (OAC), and proactive Amazon CloudWatch metric alarms.

Comprehensive functional, integration, security, and load testing demonstrates that ReFynd achieves sub-100ms API response latencies, guarantees 100% data isolation for private user credentials, mitigates common web vulnerabilities (SQL injection, Cross-Site Scripting, and automated spam via token-bucket rate limiting), and operates within a highly cost-effective cloud budget of approximately \$21.00 per month. ReFynd represents a turnkey, enterprise-ready digital transformation of campus lost-and-found management.

**Keywords:** Cloud Computing, DevOps, Terraform, Amazon Web Services (AWS), ECS Fargate, Docker, FastAPI, React, PostgreSQL, Privacy-Preserving Architecture, Amazon Rekognition, CI/CD.

\newpage

---

## TABLE OF CONTENTS

| Chapter No. | Title | Page No. |
| :--- | :--- | :--- |
| | **BONAFIDE CERTIFICATE** | ii |
| | **DECLARATION** | iii |
| | **ACKNOWLEDGEMENT** | iv |
| | **ABSTRACT** | v |
| | **TABLE OF CONTENTS** | vi |
| | **LIST OF FIGURES** | ix |
| | **LIST OF TABLES** | xi |
| | **LIST OF ABBREVIATIONS** | xii |
| **1** | **INTRODUCTION** | **1** |
| | 1.1 Introduction to the Project | 1 |
| | 1.2 Background of the Lost-and-Found Problem | 2 |
| | 1.3 Motivation | 4 |
| | 1.4 Overview of the ReFynd Platform | 5 |
| | 1.5 Scope of the Project | 6 |
| | 1.6 Significance and Real-World Applications | 7 |
| | 1.7 Organization of the Report | 8 |
| **2** | **LITERATURE REVIEW** | **9** |
| | 2.1 Introduction to Literature Review | 9 |
| | 2.2 Survey of Existing Lost-and-Found Systems | 10 |
| | 2.3 Detailed Analysis of Research Paper 1 | 11 |
| | 2.4 Detailed Analysis of Research Paper 2 | 13 |
| | 2.5 Detailed Analysis of Research Paper 3 | 15 |
| | 2.6 Detailed Analysis of Research Paper 4 | 16 |
| | 2.7 Comparative Analysis Matrix of Existing Solutions | 18 |
| | 2.8 Critical Limitations of Existing Approaches | 20 |
| | 2.9 Research Gap Identification | 21 |
| | 2.10 How ReFynd Addresses the Identified Research Gap | 22 |
| **3** | **PROBLEM STATEMENT AND OBJECTIVES** | **23** |
| | 3.1 Problem Identification | 23 |
| | 3.2 Formal Problem Statement | 24 |
| | 3.3 Project Objectives | 25 |
| | 3.4 Workflow of the Existing Legacy System | 26 |
| | 3.5 Limitations of the Existing System | 27 |
| | 3.6 Proposed ReFynd System Architecture | 28 |
| | 3.7 Engineering Advantages of the Proposed System | 29 |
| **4** | **METHODOLOGY AND SYSTEM REQUIREMENTS** | **31** |
| | 4.1 Software Engineering Methodology (Agile & DevOps) | 31 |
| | 4.2 Stakeholder and Requirement Analysis | 33 |
| | 4.3 Functional Requirements (FR) | 34 |
| | 4.4 Non-Functional Requirements (NFR) | 36 |
| | 4.5 Hardware Requirements | 38 |
| | 4.6 Software Requirements and Dependency Stack | 39 |
| | 4.7 Technology Selection Matrix and Justification | 40 |
| | 4.8 End-to-End Development and Deployment Workflow | 42 |
| | 4.9 Project Roles and Responsibilities | 43 |
| **5** | **SYSTEM DESIGN AND ARCHITECTURE** | **44** |
| | 5.1 System Architecture Overview | 44 |
| | 5.2 High-Level Architecture Diagram | 45 |
| | 5.3 Frontend Component Architecture | 47 |
| | 5.4 Backend Microservices Architecture | 49 |
| | 5.5 Database Architecture and VPC Placement | 51 |
| | 5.6 Use-Case Modeling and Actor Specifications | 52 |
| | 5.7 Data Flow Diagrams (DFD Level 0, Level 1, Level 2) | 55 |
| | 5.8 Entity-Relationship Diagram (ERD) | 58 |
| | 5.9 Detailed Database Schema and Data Dictionary | 60 |
| | 5.10 RESTful API Architecture and OpenAPI Contracts | 64 |
| | 5.11 Multi-Layer Defense-in-Depth Security Architecture | 66 |
| **6** | **SYSTEM IMPLEMENTATION** | **68** |
| | 6.1 Development Environment Setup | 68 |
| | 6.2 Frontend Implementation (React 18, TypeScript, Tailwind) | 69 |
| | 6.3 State Management, Routing, and Error Boundaries | 71 |
| | 6.4 Backend Implementation with FastAPI and Python 3.11 | 73 |
| | 6.5 Data Validation and Serialization with Pydantic v2 | 75 |
| | 6.6 Asynchronous Persistence with SQLAlchemy 2.0 & Asyncpg | 77 |
| | 6.7 Database Migrations and Seeding with Alembic | 78 |
| | 6.8 Authentication, Role-Based Access Control, and JWT | 79 |
| | 6.9 Lost and Found Reporting Workflows | 81 |
| | 6.10 Intelligent Item Matching Engine | 83 |
| | 6.11 Image Ingestion Pipeline and Amazon Rekognition Moderation | 85 |
| | 6.12 Administrative Dashboard and Claim Adjudication | 87 |
| | 6.13 Application-Level Rate Limiting with SlowAPI | 89 |
| | 6.14 Live Asynchronous Email Notifications via BackgroundTasks | 91 |
| **7** | **CLOUD AND DEVOPS IMPLEMENTATION** | **93** |
| | 7.1 Introduction to Cloud-Native DevOps | 93 |
| | 7.2 Version Control and Branching Strategy with Git & GitHub | 94 |
| | 7.3 Multi-Stage Docker Containerization | 95 |
| | 7.4 Multi-Container Local Orchestration with Docker Compose | 97 |
| | 7.5 Continuous Integration with GitHub Actions | 98 |
| | 7.6 Architectural Evolution: From Temporary Serverless to AWS | 100 |
| | 7.7 AWS Infrastructure Topology and VPC Networking | 102 |
| | 7.8 Container Orchestration: Amazon ECR and ECS Fargate | 104 |
| | 7.9 Edge Content Delivery: Amazon CloudFront CDN and S3 | 106 |
| | 7.10 Managed Database Tier: Amazon RDS PostgreSQL 16 | 108 |
| | 7.11 Infrastructure as Code (IaC) with Terraform | 109 |
| | 7.12 Identity & Access Management (IAM) and Security Hardening | 111 |
| | 7.13 Proactive Monitoring with CloudWatch and SNS Alarms | 112 |
| | 7.14 Zero-Downtime Deployment Workflow | 113 |
| **8** | **VERIFICATION, TESTING, AND RESULTS** | **115** |
| | 8.1 Testing Strategy and Verification Objectives | 115 |
| | 8.2 Unit and API Testing with Pytest | 116 |
| | 8.3 Integration and Database Transactional Testing | 118 |
| | 8.4 User Interface and Usability Testing | 119 |
| | 8.5 Security Vulnerability and Penetration Testing | 120 |
| | 8.6 Live Production Verification on AWS Cloud | 122 |
| | 8.7 Comprehensive Test Case Execution Matrix | 123 |
| | 8.8 Production Incident Resolution and Case Studies | 127 |
| | 8.9 System Performance and Latency Evaluation | 129 |
| **9** | **CONCLUSION AND FUTURE SCOPE** | **131** |
| | 9.1 Project Conclusion | 131 |
| | 9.2 Key Achievements | 132 |
| | 9.3 System Limitations | 133 |
| | 9.4 Future Work and Research Directions | 134 |
| | **REFERENCES** | **136** |
| | **APPENDICES** | **140** |
| | Appendix A: Complete PostgreSQL DDL Schema Definitions | 140 |
| | Appendix B: Core API Endpoints and Payload Specifications | 143 |
| | Appendix C: Main Terraform Infrastructure Blueprint | 145 |
| | Appendix D: Production Docker Configurations | 148 |
| | Appendix E: User Manual and Deployment Guide | 150 |

\newpage

---

## LIST OF FIGURES

| Figure No. | Caption | Page No. |
| :--- | :--- | :--- |
| Figure 1.1 | High-Level Operational Overview of the ReFynd Platform | 5 |
| Figure 3.1 | Traditional Campus Lost-and-Found Workflow (Legacy System) | 26 |
| Figure 4.1 | Agile Scrum and DevOps Continuous Engineering Lifecycle | 32 |
| Figure 4.2 | ReFynd Technology Stack Decomposition | 41 |
| Figure 5.1 | Three-Tier High-Level Cloud Architecture of ReFynd on AWS | 46 |
| Figure 5.2 | Frontend Component Hierarchy and State Flow | 48 |
| Figure 5.3 | FastAPI Asynchronous Request-Response Pipeline | 50 |
| Figure 5.4 | Comprehensive UML Use-Case Diagram for ReFynd System | 53 |
| Figure 5.5 | Data Flow Diagram (DFD) — Level 0 Context Diagram | 56 |
| Figure 5.6 | Data Flow Diagram (DFD) — Level 1 Subsystem Interaction | 57 |
| Figure 5.7 | Data Flow Diagram (DFD) — Level 2 Item Reporting and Moderation | 58 |
| Figure 5.8 | Entity-Relationship Diagram (ERD) with Crow's Foot Cardinalities | 59 |
| Figure 5.9 | Multi-Layer Defense-in-Depth Security Architecture | 67 |
| Figure 6.1 | Multi-Step Lost Item Reporting User Interface Workflow | 82 |
| Figure 6.2 | Intelligent Item Matching Score Computation Pipeline | 84 |
| Figure 6.3 | Amazon Rekognition Fail-Closed Image Moderation Architecture | 86 |
| Figure 6.4 | Administrative Moderation and Claim Resolution Interface | 88 |
| Figure 6.5 | Asynchronous Email Notification Dispatch Sequence | 92 |
| Figure 7.1 | Multi-Stage Docker Container Build Optimization Pipeline | 96 |
| Figure 7.2 | Continuous Integration Workflow via GitHub Actions | 99 |
| Figure 7.3 | Architectural Comparison: Serverless Prototyping vs. Dedicated AWS Stack | 101 |
| Figure 7.4 | AWS Virtual Private Cloud (VPC) Subnet Isolation Topology | 103 |
| Figure 7.5 | Amazon ECS Fargate Container Orchestration Architecture | 105 |
| Figure 7.6 | CloudFront CDN Edge Routing and Single-Page Application Fallback | 107 |
| Figure 7.7 | Terraform Infrastructure as Code Provisioning Flow | 110 |
| Figure 7.8 | CloudWatch Metric Alarms and SNS Notification Pipeline | 113 |
| Figure 8.1 | Automated Test Execution Pipeline Passing 18/18 Unit Test Cases | 117 |
| Figure 8.2 | Production Verification: Report Confirmation Email in Gmail Inbox | 122 |
| Figure 8.3 | Production Verification: Support Ticket Forwarding to Platform Admin | 123 |
| Figure 8.4 | CloudFront CDN and ECS Backend Latency Benchmark Curves | 130 |

\newpage

---

## LIST OF TABLES

| Table No. | Caption | Page No. |
| :--- | :--- | :--- |
| Table 2.1 | Feature Comparison Matrix of Existing Lost-and-Found Systems vs ReFynd | 19 |
| Table 4.1 | Minimum Hardware Specifications for Development, CI, and Cloud Compute | 38 |
| Table 4.2 | Software Stack and Dependency Framework Versions | 39 |
| Table 4.3 | Technology Selection and Architectural Trade-off Evaluation | 41 |
| Table 4.4 | Team Roles and Engineering Responsibilities Allocation | 43 |
| Table 5.1 | Data Dictionary: `users` Table | 60 |
| Table 5.2 | Data Dictionary: `lost_items` Table | 61 |
| Table 5.3 | Data Dictionary: `found_items` Table | 62 |
| Table 5.4 | Data Dictionary: `claims` Table | 63 |
| Table 5.5 | Data Dictionary: `matches` Table | 63 |
| Table 5.6 | Data Dictionary: `support_tickets` Table | 64 |
| Table 5.7 | Core RESTful API Routes and HTTP Method Matrix | 65 |
| Table 6.1 | Rate Limiting Policy and Enforcement Thresholds | 90 |
| Table 7.1 | AWS Cloud Infrastructure Bill of Materials (BoM) and Resource Inventory | 104 |
| Table 7.2 | CloudWatch Production Metric Alarms Configuration | 112 |
| Table 7.3 | Monthly Cloud Infrastructure Cost Optimization Breakdown | 114 |
| Table 8.1 | Comprehensive Verification and Test Case Execution Results (TC-01 to TC-25) | 124 |
| Table 8.2 | Summary of Historical Engineering Bugs and Architectural Fixes | 128 |
| Table 8.3 | End-to-End Latency Benchmark Measurements Under Variable Concurrency | 130 |

\newpage

---

## LIST OF ABBREVIATIONS

| Abbreviation | Expanded Description |
| :--- | :--- |
| **ACID** | Atomicity, Consistency, Isolation, Durability |
| **ALB** | Application Load Balancer (AWS) |
| **API** | Application Programming Interface |
| **ARM** | Advanced RISC Machine (Processor Architecture) |
| **AWS** | Amazon Web Services |
| **CDN** | Content Delivery Network |
| **CI/CD** | Continuous Integration / Continuous Deployment |
| **CORS** | Cross-Origin Resource Sharing |
| **CSRF** | Cross-Site Request Forgery |
| **CSS** | Cascading Style Sheets |
| **DDL** | Data Definition Language |
| **DFD** | Data Flow Diagram |
| **ECR** | Amazon Elastic Container Registry |
| **ECS** | Amazon Elastic Container Service |
| **ERD** | Entity-Relationship Diagram |
| **Fargate** | AWS Serverless Compute Engine for Containers |
| **HTML** | HyperText Markup Language |
| **HTTP** | HyperText Transfer Protocol |
| **HTTPS** | HyperText Transfer Protocol Secure |
| **IaC** | Infrastructure as Code |
| **IAM** | Identity and Access Management |
| **IP** | Internet Protocol |
| **JSON** | JavaScript Object Notation |
| **JWT** | JSON Web Token |
| **NFR** | Non-Functional Requirement |
| **Nginx** | High-Performance HTTP Server and Reverse Proxy |
| **OAC** | Origin Access Control (Amazon CloudFront) |
| **ORM** | Object-Relational Mapping |
| **PII** | Personally Identifiable Information |
| **PostgreSQL** | Advanced Open-Source Relational Database Management System |
| **RAM** | Random Access Memory |
| **RBAC** | Role-Based Access Control |
| **RDS** | Amazon Relational Database Service |
| **REST** | Representational State Transfer |
| **S3** | Amazon Simple Storage Service |
| **SDLC** | Software Development Life Cycle |
| **SLA** | Service Level Agreement |
| **SMTP** | Simple Mail Transfer Protocol |
| **SNS** | Amazon Simple Notification Service |
| **SPA** | Single-Page Application |
| **SQL** | Structured Query Language |
| **TLS** | Transport Layer Security |
| **UI/UX** | User Interface / User Experience |
| **URI** | Uniform Resource Identifier |
| **URL** | Uniform Resource Locator |
| **UUID** | Universally Unique Identifier |
| **VPC** | Virtual Private Cloud |
| **WAF** | Web Application Firewall |
| **XSS** | Cross-Site Scripting |

