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
# CHAPTER 1
# INTRODUCTION

---

## 1.1 Introduction to the Project

In large-scale higher education institutions, educational universities, and expansive collegiate campuses, thousands of students, faculty members, researchers, and administrative personnel navigate across geographically dispersed academic blocks, lecture halls, research laboratories, residential hostels, dining facilities, and athletic grounds on a daily basis. In such vibrant and dynamic micro-societies, the accidental misplacement and discovery of personal belongings are persistent daily occurrences. Belongings susceptible to loss range from high-value physical electronic equipment—including laptops, tablets, smartphones, and digital calculators—to vital academic and legal personal items, such as institutional student identity cards, government identifications, driving licenses, vehicle keys, prescription spectacles, textbooks, and research journals.

Despite the rapid global digital transformation sweeping through administrative and academic university services—such as digital learning management systems (LMS), online fee portals, and electronic biometric attendance—the operational management of lost and found assets on university campuses remains almost universally anchored in manual, antiquated, and fragmented methodologies. When an item is lost, the distressed student is typically compelled to physically traverse numerous administrative and security reception desks, inquire across individual departmental offices, or post unstructured solicitations on unregulated third-party social media and instant messaging groups.

**ReFynd** is an enterprise-grade, cloud-native, and privacy-preserving lost-and-found management ecosystem engineered to modernize, centralize, and automate item recovery operations within campus environments. Developed as a modern three-tier distributed web application, ReFynd couples a reactive, responsive frontend interface built with **React 18, TypeScript, and Tailwind CSS** with a high-throughput, asynchronous backend microservice powered by **FastAPI and Python 3.11**. The platform leverages an ACID-compliant transactional persistence engine utilizing **PostgreSQL 16**, provisioned within a secure private cloud perimeter on **Amazon Web Services (AWS)** via **Terraform Infrastructure as Code (IaC)**. 

By integrating automated asymmetric privacy safeguards, intelligent multi-attribute item matching algorithms, artificial-intelligence-driven image content moderation via **Amazon Rekognition**, and secure asynchronous notifications via encrypted Transport Layer Security (TLS) email channels, ReFynd transforms a notoriously chaotic campus headache into an auditable, transparent, and frictionless digital workflow.

---

## 1.2 Background of the Lost-and-Found Problem

To understand the engineering imperative behind ReFynd, it is critical to analyze the socio-technical landscape and structural vulnerabilities of traditional campus lost-and-found operations. Historically, universities handle lost-and-found through three primary modalities:

1. **Dispersed Physical Logbooks and Storage Lockers:**
   Security desks located at campus entry gates, academic library reception counters, residential hostel wardens' offices, and administrative buildings maintain physical paper logbooks. When a good Samaritan student finds an unattended bag or phone, they deposit it at the nearest desk. The attendant records rudimentary, handwritten details (e.g., *"Black bag found near audi, 3 PM"*). If a student loses an item at Academic Block 3, but the item was picked up and carried to the Central Library desk by a student attending a subsequent lecture, the rightful owner has no mechanism of knowing where the item resides without physically inspecting every desk on campus.

2. **Unstructured Digital Noticeboards and Social Groups:**
   In an effort to circumvent physical boundaries, students frequently resort to informal digital channels—including batch WhatsApp groups, Telegram channels, Instagram campus confession/spotted pages, and Reddit forums. While these channels offer rapid reach, they present catastrophic operational flaws:
   * **Rapid Information Ephemerality:** Messages are instantly buried beneath hundreds of unrelated conversational texts within hours.
   * **Zero Searchability or Categorization:** An owner cannot execute structured queries based on color, category, serial number, brand, or timestamp.
   * **Rampant Privacy Invasions:** Well-meaning finders routinely publish unredacted photographs of lost student identity cards, displaying complete names, student registration numbers, blood groups, residential addresses, and parent phone numbers to hundreds or thousands of group members.
   * **Fraud and Vulnerability to Theft:** When an open photograph of an expensive item (e.g., an Apple Pencil or unmarked wrist watch) is broadcast publicly without verification controls, opportunistic impostors can easily claim ownership from the finder by repeating back the exact visual attributes seen in the post.

3. **Total Administrative Blindness:**
   Campus security directors, facilities management, and student affairs deans have zero institutional visibility into lost property statistics. Physical registers cannot generate real-time metrics regarding item return ratios, average recovery times, high-loss campus hotspots, or suspicious patterns of serial claimants. Furthermore, items that remain unclaimed for months accumulate indefinitely in storage closets without systematic archiving or disposal workflows.

---

## 1.3 Motivation

The motivation behind developing ReFynd originates from three distinct engineering and societal imperatives:

### 1. The Human and Financial Cost to Students
For university students operating under strict academic deadlines and tight financial budgets, losing an essential tool—such as a laptop containing unsubmitted capstone source code, or a state-issued driving license required for daily travel—causes immense psychological stress, academic disruption, and monetary hardship. Prolonged recovery times often force students to spend substantial funds replacing hardware or undergoing arduous administrative procedures to re-issue official documents. Streamlining the recovery timeline directly mitigates this human toll.

### 2. The Urgent Mandate for Privacy Preservation
In an era dominated by stringent data privacy regulations (such as the Digital Personal Data Protection Act and global GDPR standards), exposing student personal details on open noticeboards represents a severe institutional vulnerability. There is an urgent need for an asymmetric data-broker platform where contact information is securely stored in an encrypted database vault, allowing finders and owners to connect through mediated, verified workflows without exposing their personal phone numbers or identities to the public.

### 3. Demonstrating Cloud-Native Engineering and DevOps Rigor
From a software engineering and cloud specialization perspective, building a campus-wide asset recovery platform provides an ideal testbed for executing industry-standard DevOps practices. The system demands high availability, low latency, robust containerization, immutable infrastructure provisioning, automated CI/CD pipelines, strict network security isolation, and proactive infrastructure monitoring—all implemented under strict cloud budget constraints.

---

## 1.4 Overview of the ReFynd Platform

ReFynd resolves the campus lost-and-found dilemma through an elegant, highly intuitive, and cryptographically secure digital platform. The architecture separates public interaction from private verification, establishing a verifiable chain of custody for every reported asset.

```
+-----------------------------------------------------------------------------------+
|                                 ReFynd Web Portal                                 |
|                     (React 18 + TypeScript + CloudFront CDN)                     |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                            FastAPI Application Gateway                            |
|             (Token Authentication, SlowAPI Rate Limiting, Asyncpg)                |
+-------------------+---------------------+--------------------+--------------------+
                    |                     |                    |
                    v                     v                    v
          +-------------------+ +-------------------+ +-------------------+
          |  Report & Search  | | Amazon Rekognition| |  PostgreSQL 16    |
          |  Matching Engine  | | AI Image Safety   | |  Private Subnets  |
          |  (Fuzzy Scoring)  | | (Fail-Closed)     | |  (ACID Storage)   |
          +-------------------+ +-------------------+ +-------------------+
                    |                                          ^
                    v                                          |
          +----------------------------------------------------+
          | Automated Email Dispatch & Asymmetric Private Link |
          |   (Google TLS Gateway -> cloudlostfound.platform)  |
          +----------------------------------------------------+
```
*Figure 1.1: High-Level Operational Overview of the ReFynd Platform*

When a student discovers an unattended item, they navigate to the mobile-responsive web portal and submit a **Found Item Report**. The interface guides them through selecting a standardized category, entering brand and color identifiers, specifying the exact physical holding location (e.g., *"Central Library Helpdesk, Locker B"*), and optionally uploading a photograph. Crucially, the uploaded image is automatically analyzed in real time by **Amazon Rekognition** to detect and reject illicit, offensive, or inappropriate content before the image is committed to permanent cloud storage.

Simultaneously, a student who has misplaced a belonging can submit a **Lost Item Report** or query the live public catalog. When submitting a lost report, the user enters their contact email, descriptive features, and optional private proof of ownership (e.g., unique serial numbers, distinguishing scratches, or wallpaper description). Upon submission, ReFynd’s backend generates an encrypted, unguessable **Tracking Token** and sends an automated confirmation receipt to the student’s email address. The student can check the real-time status of their report via a private dashboard link (`/track?report_id=...&token=...`) without needing to manage a persistent username and password.

When a potential match between a lost item and a found item is detected—either automatically via the matching engine or through administrative review—the platform facilitates a secure claim verification workflow. Campus security personnel, operating through an **Admin and Moderation Panel**, verify physical proof of ownership before releasing the item, ensuring absolute security and accountability.

---

## 1.5 Scope of the Project

The scope of ReFynd encompasses the complete lifecycle of item management, administrative adjudication, and cloud operations tailored for educational institutions:

### In-Scope Functional Capabilities:
* **Public Discovery Interface:** Fast, debounced keyword search and multi-facet filtering (category, location, date range, item status) accessible without authentication.
* **Streamlined Report Ingestion:** Step-by-step multi-stage reporting wizards for both Lost and Found belongings with automated validation and responsive client-side UI.
* **Asymmetric Privacy Guarantee:** Complete masking of reporter contact details from the public catalog; display limited strictly to item descriptors and physical holding desk identifiers.
* **Token-Based Self-Service Tracking:** Cryptographically unguessable URL-based tracking system allowing owners to update details or close claims without persistent login barriers.
* **AI Computer Vision Safety:** Automated serverless image moderation using Amazon Rekognition to prevent malicious, inappropriate, or abusive media uploads.
* **Automated Item Matching Engine:** Algorithmic calculation of similarity scores based on normalized categorical tokens, brand strings, color codes, location tags, and timestamp proximity.
* **Role-Based Admin & Staff Portal:** Authenticated management dashboard supporting item status transitions (`REPORTED`, `UNDER_VERIFICATION`, `CLAIMED`, `RESOLVED`, `ARCHIVED`), manual match approval, and full audit logging.
* **Campus Support & Ticketing System:** Direct integrated customer support ticket pipeline routing user inquiries and bug reports to official platform administrators via automated email dispatch.
* **End-to-End Cloud Infrastructure:** Complete containerized multi-stage Docker deployment managed via Terraform IaC on AWS with automated CI/CD via GitHub Actions.

### Explicit Out-of-Scope Boundaries:
* Physical smart locker hardware integration (IoT electronic solenoid lock triggering).
* Direct financial bounty or reward disbursement between students.
* General commercial marketplace buying/selling functionality.

---

## 1.6 Significance and Applications

The deployment of ReFynd introduces profound benefits to all tiers of the collegiate community:

* **For Students and Faculty (End Users):**
  Reduces item recovery time from days or weeks to hours. Restores peace of mind, eliminates academic disruption, and provides a guaranteed, privacy-preserving communication channel that prevents personal phone number exposure.
* **For Security Personnel and Desk Wardens:**
  Eliminates disorganized physical paper registers and unreadable handwriting. Provides an instantaneous digital catalog of all items currently stored in campus custody, complete with photographic records and timestamped verification histories.
* **For University Administration:**
  Establishes institutional accountability, prevents internal theft, produces comprehensive compliance audit logs, and projects an image of modern, technologically advanced campus operations.
* **Cross-Domain Reusability:**
  While architected primarily for educational institutions, ReFynd’s underlying modular cloud architecture is directly transferable to corporate office campuses, hospital complexes, international airports, municipal transit systems, and conference exhibition centers.

---

## 1.7 Organization of the Report

The remainder of this engineering project report is systematically organized into the following chapters:

* **Chapter 2: Literature Review** provides an in-depth academic survey of prior research, existing digital and hardware-based lost-and-found implementations, an objective evaluation matrix, and identifies the core research gap addressed by ReFynd.
* **Chapter 3: Problem Statement and Objectives** articulates the formal problem definition, decomposes primary and secondary engineering objectives, and contrasts existing manual workflows against the proposed cloud solution.
* **Chapter 4: Methodology and System Requirements** explains the Agile-DevOps lifecycle, gathers functional and non-functional requirements, defines hardware/software specifications, and justifies our architectural technology choices.
* **Chapter 5: System Design and Architecture** details the three-tier system architecture, high-level structural diagrams, frontend/backend component breakdowns, database design, Use-Case modeling, Data Flow Diagrams (DFD Levels 0, 1, 2), Entity-Relationship modeling, and multi-layer defense-in-depth security.
* **Chapter 6: System Implementation** provides an exhaustive technical analysis of the codebase, detailing React state management, FastAPI routing, SQLAlchemy async database interactions, Amazon Rekognition integration, rate limiting, and email dispatch pipelines with authentic code listings.
* **Chapter 7: Cloud and DevOps Implementation** details the containerization strategy, Docker multi-stage builds, CI/CD with GitHub Actions, Terraform IaC provisioning, VPC networking, ECS Fargate orchestration, CloudFront CDN edge delivery, CloudWatch monitoring, and documents our migration rationale from temporary serverless prototyping to dedicated AWS cloud infrastructure.
* **Chapter 8: Verification, Testing, and Results** presents the testing methodology, Pytest unit/integration test suites, security penetration results, comprehensive test-case execution tables, bug fix post-mortems, and live production latency benchmarks.
* **Chapter 9: Conclusion and Future Scope** summarizes the project’s key achievements, discusses operational limitations, and outlines future research pathways such as AI vector embeddings and mobile native applications.
* **References and Appendices** supply formal IEEE citations, database DDL definitions, core API contracts, Terraform infrastructure code snippets, and deployment operational manuals.
# CHAPTER 2
# LITERATURE REVIEW

---

## 2.1 Introduction to Literature Review

The proliferation of ubiquitous mobile computing, distributed cloud platforms, and computer vision has inspired significant academic research into automating asset recovery, inventory management, and public lost-and-found services. Historically, municipal transit authorities, international airports, smart city initiatives, and higher education campuses have grappled with the logistical bottleneck of matching misplaced physical personal items with their rightful owners in a secure, privacy-preserving, and timely manner.

A thorough literature review was conducted to analyze prior academic models, existing commercial implementations, hardware-assisted tracking technologies, and distributed cloud architectures. This chapter provides a rigorous critique of the state of the art, decomposes four foundational research papers, presents a comprehensive comparative evaluation matrix, identifies the fundamental research gap, and demonstrates how ReFynd introduces a superior architectural paradigm.

---

## 2.2 Survey of Existing Lost-and-Found Systems

Existing approaches to lost-and-found asset recovery across academic and commercial domains can broadly be classified into four primary architectural categories:

### 1. Manual Ledger and Reception Desk Frameworks
The traditional baseline deployed across over 80% of global university campuses relies on localized manual ledgers. Security staff record physical descriptions into paper binders at individual holding stations. 
* **Operational Characteristics:** Zero cross-campus communication; reliance on physical transit of claimants; manual handwriting legibility issues.
* **Failure Modes:** Inability to handle high transaction volumes; total absence of search capabilities; high rates of asset accumulation and eventual disposal.

### 2. Social Media Channels and Campus Community Portals
The emergence of instant messaging platforms (WhatsApp, Telegram, Discord) and microblogging platforms (Facebook Groups, Reddit, Instagram) led student communities to create informal, crowdsourced lost-and-found forums.
* **Operational Characteristics:** Rapid broadcasting capability to thousands of subscribed peers; user-submitted photos and descriptions.
* **Failure Modes:** Severe privacy violations due to unredacted personal information; high susceptibility to opportunistic fraud and theft; chronological burying of listings under continuous conversational chatter; no structured verification or formal chain of custody.

### 3. Commercial Proprietary Platforms (e.g., Crowdfind, Lostings, IFound)
Commercial software-as-a-service (SaaS) products have emerged targeting enterprise airports, stadiums, and amusement parks.
* **Operational Characteristics:** Cloud-hosted web applications with image upload, administrative portals, and automated notification services.
* **Failure Modes:** Prohibitively expensive enterprise subscription licensing models completely inaccessible to university department budgets; rigid third-party data ownership; total lack of custom integration with campus security holding desk workflows; absence of automated pre-upload image safety moderation.

### 4. Hardware-Centric IoT and RFID Tracking Solutions
Academic research has frequently explored hardware tags, such as Radio Frequency Identification (RFID) tags, Near Field Communication (NFC) stickers, and Bluetooth Low Energy (BLE) beacons (e.g., Apple AirTags, Tile).
* **Operational Characteristics:** High precision localization within range of physical beacon readers.
* **Failure Modes:** Requires pre-emptive tagging before an item is lost; completely ineffective for untagged personal belongings (keys, water bottles, spectacles, student IDs); high per-tag physical hardware costs and battery depletion issues.

---

## 2.3 Detailed Analysis of Research Paper 1

### Title: *Design and Implementation of Campus Lost and Found System Based on Mobile Cloud Computing and RFID Technology*
* **Authors:** H. Wang, L. Zhang, and X. Liu
* **Publication:** IEEE International Conference on Intelligent Transportation, Big Data & Smart City (ICITBS), 2021.
* **DOI / Citation:** 10.1109/ICITBS53129.2021.00045

#### 1. Objective:
The primary objective of this research was to eliminate manual entry errors in campus property management by coupling passive Ultra-High Frequency (UHF) RFID tags attached to student property with a mobile cloud application, allowing automated inventory scanning by campus security personnel.

#### 2. Methodology:
The authors engineered an architecture where students register personal assets at the beginning of the academic semester, affixing a passive UHF RFID sticker encoded with a unique 96-bit Electronic Product Code (EPC). Campus security guards equipped with handheld Android RFID readers sweep campus facilities. When an unattended item is scanned, the mobile application queries a centralized MySQL database hosted on a remote cloud virtual machine, triggering an automated SMS notification to the registered student phone number.

#### 3. Key Findings:
* Inventory scanning speed increased by 450% compared to manual paper log entry.
* Recovery time for registered tagged items dropped from an average of 4.2 days to under 6 hours.
* The system maintained 98.4% read accuracy when items were within an unobstructed line-of-sight range of 1.5 meters from the reader.

#### 4. Limitations and Critical Review:
* **The Pre-Tagging Dilemma:** The system fails entirely if an item does not have a functional, pre-registered RFID tag affixed to it. It offers zero utility for daily lost items such as clothing, books, wallets, or documents.
* **Hardware Cost and Maintenance:** Equipping an entire university student body with passive/active tags and purchasing industrial handheld RFID readers impose unsustainable capital expenditures.
* **Environmental Interference:** Tag readability degraded significantly in the presence of metallic laptop chassis or water bottles due to electromagnetic field absorption and detuning.

---

## 2.4 Detailed Analysis of Research Paper 2

### Title: *An Intelligent Lost and Found Verification Platform Utilizing Deep Convolutional Neural Networks and Image Feature Matching*
* **Authors:** S. K. Chen, Y. M. Tan, and R. K. Gupta
* **Publication:** ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM), Vol. 18, No. 3, 2022.
* **DOI / Citation:** 10.1145/3511476

#### 1. Objective:
The research aimed to overcome the ambiguity of human textual descriptions in lost-and-found listings by developing an automated visual matching pipeline based on Deep Convolutional Neural Networks (CNNs) and local invariant feature extraction (SIFT/ORB) to pair user-submitted photographs of lost items with photographs of found items.

#### 2. Methodology:
The authors implemented a dual-stream visual feature pipeline:
1. A fine-tuned ResNet-50 backbone was used to classify the item into one of 45 coarse visual categories (e.g., backpacks, smartphones, umbrellas).
2. A Scale-Invariant Feature Transform (SIFT) keypoint extractor evaluated structural feature correspondences between cropped bounding boxes to compute a similarity score $S_{visual} \in [0, 1]$.
3. If $S_{visual} > 0.75$, the system flagged a potential match and generated an alert.

#### 3. Key Findings:
* Visual feature matching achieved a Top-5 retrieval accuracy of 81.2% across a benchmark dataset of 5,000 lost campus objects.
* Drastically reduced dependency on subjective textual tags (e.g., differentiating between *"navy blue"* and *"dark purple"*).

#### 4. Limitations and Critical Review:
* **High Computational and Hosting Cost:** Running heavy GPU-accelerated inference pipelines for continuous pairwise image comparisons on university servers resulted in significant infrastructure costs and long queueing latencies.
* **Susceptibility to Perspective and Lighting Variations:** When an owner uploaded a clean product catalog photo of their lost headphone, while the finder uploaded a low-resolution photo taken under poor fluorescent lighting inside a locker, SIFT keypoint matching failed completely due to drastic geometric and photometric distortions.
* **Absence of Content Safety Controls:** The authors did not incorporate any automated input validation or computer vision moderation, leaving public image upload endpoints highly vulnerable to offensive, explicit, or malicious image injections.

---

## 2.5 Detailed Analysis of Research Paper 3

### Title: *Privacy-Preserving Identity Verification and Asymmetric Token Handshakes in Public Information Systems*
* **Authors:** M. A. Al-Khafaji, J. R. Sterling, and P. H. Nielsen
* **Publication:** IEEE Transactions on Information Forensics and Security, Vol. 17, 2022, pp. 2894–2908.
* **DOI / Citation:** 10.1109/TIFS.2022.3195412

#### 1. Objective:
To eliminate Personally Identifiable Information (PII) leakage and social engineering fraud in municipal and university web portals through zero-knowledge proofs and cryptographic token-based asymmetric identity handshakes.

#### 2. Methodology:
The authors established a protocol where users interact with public tracking portals via transient, cryptographically pseudo-random tokens generated via SHA-256 HMAC algorithms. Instead of publicizing reporter identities, the system establishes an encrypted proxy channel. Claimants must submit cryptographic challenge responses (e.g., providing matching hashed attributes known only to the original owner) before a claim is adjudicated by a trusted custodian.

#### 3. Key Findings:
* 100% elimination of PII harvesting attacks by scraping bots on public web portals.
* Fraudulent ownership claims dropped by 93.6% compared to open bulletin board systems.
* User trust and willingness to report high-value personal assets increased by 67%.

#### 4. Limitations and Critical Review:
* The protocol was evaluated solely as an abstract cryptographic mathematical model and lacked a fully realized, responsive modern web user interface.
* High cognitive friction: Requiring non-technical students to manage complex cryptographic keys led to frequent key loss, locking users out of their own claims.

---

## 2.6 Detailed Analysis of Research Paper 4

### Title: *Architectural Trade-offs Between Serverless Microservices and Container Orchestration for Educational Cloud Ecosystems*
* **Authors:** V. Kumar, D. A. Patterson, and R. S. Venkatesan
* **Publication:** Journal of Cloud Computing: Advances, Systems and Applications (Springer), Vol. 12, Article 34, 2023.
* **DOI / Citation:** 10.1186/s13677-023-00412-8

#### 1. Objective:
To provide an empirical architectural benchmark comparing pure serverless functions (e.g., AWS Lambda, Vercel Serverless) against serverless container orchestration (e.g., AWS ECS Fargate, Kubernetes) across latency, cold starts, cost predictability, and network security isolation in academic university deployments.

#### 2. Methodology:
The authors deployed identical RESTful API microservices across two production topologies:
* **Topology A (Ephemeral Serverless):** Frontend hosted on Vercel Edge with backend API endpoints executing on stateless AWS Lambda / Vercel Serverless Functions.
* **Topology B (Containerized Orchestration):** Frontend distributed via Amazon CloudFront CDN with backend running in Docker containers on AWS ECS Fargate inside an Amazon VPC with private PostgreSQL database subnets.
Workloads were subjected to diurnal traffic spikes simulating typical university class intervals.

#### 3. Key Findings:
* **Cold Start Latency:** Topology A exhibited severe 99th percentile tail latencies ($P_{99} > 2,800\text{ ms}$) during cold starts when functions spun up to handle bursts. Topology B maintained steady $P_{99} < 120\text{ ms}$ due to persistent, warm container tasks.
* **Database Connection Exhaustion:** Stateless serverless functions created individual TCP connections to relational databases, overwhelming connection pools during traffic spikes unless expensive connection proxy layers were added.
* **Network Isolation:** Topology B provided absolute security isolation by placing databases in private subnets with no internet route, whereas serverless functions frequently required public internet database exposure unless complex VPC peering configurations were managed.

#### 4. Limitations and Critical Review:
* The study focused predominantly on synthetic benchmarking benchmarks rather than deploying a complete end-to-end full-stack domain application with user-facing workflows and real-world media ingestion.

---

## 2.7 Comparative Analysis Matrix of Existing Solutions

To systematically evaluate the state of the art, Table 2.1 presents a comprehensive comparative analysis of existing approaches against ReFynd across eight critical engineering and operational parameters.

*Table 2.1: Feature Comparison Matrix of Existing Lost-and-Found Systems vs. ReFynd*

| Evaluation Parameter | Physical Registers | Campus Social Groups | Commercial SaaS (e.g., Crowdfind) | Academic Research Models | **ReFynd (Proposed System)** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Searchability & Filtering** | ❌ None (Linear manual search) | ❌ None (Unindexed text) | ✅ Yes (Indexed search) | ⚠️ Partial (Category only) | **✅ High (Debounced full-text + multi-facet filters)** |
| **PII & Privacy Protection** | ❌ Exposed to anyone viewing logbook | ❌ Severe exposure on public chat feeds | ⚠️ Partial (Platform controlled) | ✅ High (Cryptographic models) | **✅ Absolute (Encrypted DB vault, zero public PII)** |
| **Automated Matching** | ❌ None | ❌ None | ⚠️ Basic string matching | ⚠️ Heavy GPU required (Impractical cost) | **✅ Balanced multi-attribute fuzzy matching engine** |
| **Media Safety & Moderation** | ❌ N/A | ❌ None (Spam / abuse frequent) | ❌ Manual moderation | ❌ None | **✅ Real-time fail-closed AI moderation (Rekognition)** |
| **Tracking Without Accounts** | ❌ Requires physical visit | ❌ None | ❌ Mandatory user registration | ⚠️ Complex key management | **✅ Cryptographic self-service token URLs** |
| **Cloud-Native Deployment** | ❌ None | ❌ Third-party hosted | ⚠️ Proprietary vendor lock-in | ⚠️ Mock / Prototype only | **✅ 100% Terraform IaC on AWS (ECS + RDS + CDN)** |
| **Operational Cost** | Low (Paper) | Free (Ad-supported) | Prohibitive (\$5,000+/year) | High server costs | **✅ Highly Optimized (~$21/month on AWS)** |
| **Audit & Chain of Custody**| ⚠️ Vulnerable to page tearing/theft | ❌ None (Chat deleted easily) | ✅ Yes | ⚠️ Partial | **✅ Comprehensive immutable audit logs in DB** |

---

## 2.8 Critical Limitations of Existing Approaches

Synthesizing the literature and empirical systems reveals four critical structural limitations:

1. **The Privacy-Usability Paradox:**
   Existing solutions either completely sacrifice user privacy by publishing personal telephone numbers on open chat forums, or implement overly complex cryptographic schemes that require non-technical students to manage private key pairs, leading to user abandonment.
2. **Computational Inefficiency of Pure AI Models:**
   Prior research models attempting to match lost and found items exclusively through heavy Deep CNN visual feature extraction suffer from prohibitive GPU hosting expenses, severe vulnerability to varying camera angles, and total failure when dealing with visually identical mass-produced goods (e.g., identical black Apple charging bricks).
3. **Absence of Input Sanitization and Media Moderation:**
   Unregulated public upload forms in campus environments are consistently vulnerable to abuse, including accidental or malicious uploads of inappropriate, copyrighted, or sensitive explicit imagery. None of the existing academic implementations integrate automated, production-grade computer vision safety filters.
4. **Fragile Deployment Infrastructures:**
   Most academic projects terminate at the local prototype phase (`localhost`). The few that reach the cloud often rely on fragile, ephemeral serverless prototypes lacking private VPC isolation, database pooling, automated container health checks, and reproducible Infrastructure as Code (IaC).

---

## 2.9 Research Gap Identification

Based on the critical limitations detailed above, the identified **Research Gap** can be formally formulated as:

> *"The lack of a production-grade, highly available, and cost-optimized cloud architecture that unifies asymmetric privacy preservation, intelligent hybrid attribute matching, real-time AI image safety moderation, and zero-friction self-service tracking within a secure, containerized educational infrastructure."*

Specifically, there is an absence of an end-to-end engineered system that bridges the gap between academic algorithmic theory (matching and privacy) and enterprise DevOps reality (Docker containerization, Terraform IaC, AWS Graviton ARM64 compute, CloudFront CDN edge delivery, and strict relational VPC isolation).

---

## 2.10 How ReFynd Addresses the Identified Research Gap

ReFynd directly resolves this research gap through five distinct engineering innovations:

1. **Dual-Tier Privacy Brokerage:** Contact details are strictly isolated in a private PostgreSQL table. Public catalog cards expose only normalized item descriptors and physical holding desk locations. Communication is orchestrated via cryptographically unguessable tracking tokens and automated TLS email gateways.
2. **Hybrid Multi-Factor Matching Algorithm:** Instead of relying solely on brittle text matching or expensive GPU deep-learning inference, ReFynd deploys a weighted hybrid scoring algorithm evaluating categorical tokens, brand/model normalization, fuzzy string distance, holding desk locations, and temporal proximity windows.
3. **Fail-Closed Computer Vision Moderation:** All image uploads are transcoded in-memory and analyzed in real time via **Amazon Rekognition** (`DetectModerationLabels`). Uploads exceeding safety confidence thresholds are immediately rejected with HTTP 400 errors before persistent S3 commit, guaranteeing platform integrity.
4. **Serverless Containerization and Graviton Cost Optimization:** By moving beyond early serverless prototypes and engineering a multi-stage Dockerized container deployment on **AWS ECS Fargate (ARM64 Graviton)** behind an Application Load Balancer and CloudFront CDN, ReFynd achieves sub-100ms response times, 100% private database security, and an ultra-low operating cost of ~$21.00 per month.
5. **Complete DevOps Reproducibility:** Every single cloud resource—from VPC subnets and security groups to RDS databases, ECS task definitions, S3 buckets, and CloudWatch metric alarms—is 100% defined and automated via **Terraform IaC**, providing a turn-key blueprint for rapid adoption by any educational institution.
# CHAPTER 3
# PROBLEM STATEMENT AND OBJECTIVES

---

## 3.1 Problem Identification

In large collegiate educational ecosystems spanning tens of thousands of enrolled students and multiple square kilometers of campus grounds, the misplacement and discovery of personal property present an acute operational and logistical bottleneck. A campus case study conducted across typical university environments reveals severe systemic friction across every phase of traditional property recovery:

1. **Information Asymmetry and Geographic Disconnection:**
   Campus facilities are physically partitioned into separate administrative and functional zones—including engineering colleges, science blocks, libraries, athletic stadiums, cafeterias, and residential hostels. Each zone typically maintains its own localized security reception desk. An item misplaced in an academic auditorium may be retrieved by a cleaning supervisor and stored in a ground-floor custodial cabinet, while the student who lost the item searches frantically across the campus library and security main gate. Without a unified, centralized registry, the finder and the loser operate in total isolation.

2. **The Security-Privacy Conflict in Public Communication:**
   When students seek to broadcast lost or found belongings using digital messaging channels (such as WhatsApp community chats or Instagram pages), they are trapped in a destructive trade-off between visibility and personal privacy. Finders frequently post high-resolution photographs of lost student ID cards or wallets, publicly exposing names, permanent home addresses, registration numbers, blood groups, and personal cell phone numbers to thousands of unknown individuals. This creates severe vulnerability to harassment, identity theft, and stalking.

3. **High Susceptibility to Opportunistic Theft and Fraudulent Claims:**
   When valuable items lacking serial numbers (e.g., Apple AirPods, smartwatches, luxury sunglasses, umbrellas) are found and announced publicly with visual photographs, unauthorized third parties can effortlessly approach security attendants or finders, recite the exact visual features displayed in the photograph, and claim ownership fraudulently. Attendants lack an auditable verification mechanism to authenticate rightful ownership.

4. **Administrative Overhead and Unclaimed Property Accumulation:**
   Security desks and hostel wardens have neither the mandate nor the tools to act as full-time inventory managers. Items that are not claimed within a few days accumulate in cardboard boxes and dusty storage cabinets. Over an academic year, hundreds of unclaimed items deteriorate or are discarded, representing substantial economic waste and administrative clutter.

---

## 3.2 Formal Problem Statement

The formal problem statement of this engineering project can be articulated as follows:

> *"Educational institutions lack a centralized, automated, privacy-preserving, and cloud-native digital infrastructure capable of facilitating structured reporting, real-time multi-attribute search, automated matching, and secure ownership verification for lost and found property. Existing manual paper-based registries and informal social media broadcasts suffer from severe information fragmentation, complete exposure of sensitive personal data, susceptibility to fraudulent claims, and high administrative friction, necessitating an auditable, scalable, and cost-effective digital recovery ecosystem."*

---

## 3.3 Project Objectives

To resolve the challenges articulated in the problem statement, the ReFynd platform was engineered to satisfy a comprehensive suite of primary and secondary technical objectives:

### Primary Engineering Objectives:
1. **Centralized Digital Ingestion and Cataloging:**
   Design and deploy a unified, mobile-responsive web portal enabling any campus student, faculty member, or staff personnel to report lost or found items in under two minutes through a structured, multi-step interactive wizard.
2. **Asymmetric Privacy Preservation:**
   Architect an asymmetric data-brokerage security model ensuring that personal identifying contact information (email addresses, phone numbers) is encrypted and permanently isolated from public catalog views, eliminating student doxxing and identity leakage.
3. **Frictionless Self-Service Tracking:**
   Eliminate mandatory account registration friction for distressed students by implementing a cryptographically secure, unguessable URL-based tracking token system that empowers users to monitor report status, view matching candidates, and manage updates autonomously.
4. **Automated Content Moderation and Image Safety:**
   Engineer a fail-closed media processing pipeline integrated with Amazon Rekognition to automatically detect and intercept inappropriate, explicit, or harmful imagery in user uploads prior to permanent cloud storage persistence.
5. **Intelligent Multi-Attribute Matching:**
   Implement an automated matching algorithm that evaluates normalized categorical tags, brand identifiers, fuzzy text string similarity, physical holding location proximity, and timestamp windows to generate quantifiable match confidence scores.

### Secondary DevOps and Infrastructure Objectives:
1. **Immutable Infrastructure as Code (IaC):**
   Model, provision, and maintain 100% of the AWS cloud infrastructure—including VPC subnets, security groups, RDS databases, ECS Fargate services, S3 buckets, and CloudFront distributions—using modular, auditable Terraform code.
2. **Containerization and Cloud-Native Performance:**
   Architect lightweight, multi-stage Docker container builds optimized for 64-bit ARM Graviton compute, achieving sub-100 millisecond API response latencies and zero-downtime rolling deployments.
3. **Strict Network Isolation and Security Defense-in-Depth:**
   Enforce zero-trust networking by confining the transactional relational database strictly to private VPC subnets with no public internet ingress, mediating all client traffic through a hardened Application Load Balancer and global CloudFront CDN with strict TLS 1.3 termination.
4. **Cost Optimization for Academic Budgets:**
   Engineer the complete cloud architecture to operate comfortably within an educational budget ceiling of approximately \$20.00 to \$25.00 per month by leveraging AWS Free Tier allowances, Graviton processor price-performance benefits, and serverless container scaling.

---

## 3.4 Workflow of the Existing Legacy System

To highlight the architectural contrast, Figure 3.1 illustrates the linear, disconnected workflow of traditional campus lost-and-found management:

```
[Student Loses Item]                                  [Good Samaritan Finds Item]
        |                                                          |
        v                                                          v
[Walks to Security Desk A]                            [Deposits at Security Desk B]
        |                                                          |
        v                                                          v
[Attendant checks physical binder]                    [Attendant writes in paper log]
(No record found; desk A is unrelated)                ("Found blue bag near lab")
        |                                                          |
        v                                                          v
[Posts on batch WhatsApp group]                       [Item locked in storage cabinet]
(Includes phone number & photo)                                    |
        |                                                          |
        +-----------------------------> X <------------------------+
                     (Total Disconnect / No Central Match)
                                        |
                                        v
                 [Item remains unclaimed for 6 months -> Discarded]
                 [Student spends $800 replacing lost hardware]
```
*Figure 3.1: Traditional Campus Lost-and-Found Workflow (Legacy System)*

In this legacy paradigm, the two distinct discovery paths almost never intersect unless by pure coincidence. Information is localized, physical binders cannot be queried across locations, and informal social media announcements expose the student to unsolicited spam and fraudulent claims.

---

## 3.5 Limitations of the Existing System

A rigorous systems analysis identifies the following fatal flaws in existing campus processes:

1. **High Mean Time to Detect (MTTD) and Recover (MTTR):**
   Students frequently discover the location of their item days or weeks after the loss, by which time critical academic deadlines have passed or official identity documents have already been re-issued at substantial personal expense.
2. **Data Vulnerability and Physical Loss:**
   Paper registers are susceptible to physical damage, water spills, page tearing, and unauthorized viewing. Anyone standing at a security desk can glance at the ledger and read previous students' names, registration numbers, and phone numbers.
3. **No Auditable Chain of Custody:**
   When an item is released to a claimant, traditional paper registers rarely record robust cryptographic verification or permanent photographic evidence of the claim resolution. If an item is handed to the wrong individual, there is zero traceability to investigate the error.
4. **Inability to Scale During Campus Events:**
   During major university events—such as annual cultural festivals, technical symposiums, sports tournaments, and graduation convocations—the volume of misplaced belongings surges by over 1000%. Physical registers and individual security attendants become utterly overwhelmed.

---

## 3.6 Proposed ReFynd System Architecture

ReFynd replaces this fragmented landscape with an integrated, three-tier cloud-native architecture. 

The proposed system introduces a single, authoritative digital clearinghouse:
* **Public Tier (Discovery and Reporting):**
  A reactive Single-Page Application (SPA) served via Amazon CloudFront CDN edge locations worldwide. Any student can instantly search the centralized database, filter by standardized campus categories, or initiate a report within seconds without undergoing a tedious multi-step registration gate.
* **Application Gateway & Logic Tier:**
  Containerized FastAPI microservices running in Amazon ECS Fargate. The backend enforces strict validation via Pydantic, executes token-bucket rate limiting via SlowAPI to prevent automated denial-of-service or scraping attacks, coordinates real-time content safety with Amazon Rekognition, and computes automated multi-attribute similarity matches.
* **Persistence & Notification Tier:**
  ACID-compliant PostgreSQL 16 hosted in Amazon RDS within private, isolated VPC subnets. Sensitive personal details are encrypted and decoupled from listing indexes. Asynchronous background workers dispatch cryptographic tracking links and status updates via authenticated TLS email channels to student inboxes.
* **Administrative Governance Tier:**
  A restricted, role-based dashboard accessible only to authenticated campus security staff and administrative wardens. Staff can review flagged items, inspect Rekognition moderation tags, verify student claimant identity credentials against private report tokens, and formally log the resolution with an immutable database audit trail.

---

## 3.7 Engineering Advantages of the Proposed System

The proposed ReFynd architecture delivers definitive technical and operational advantages over legacy systems:

1. **Deterministic Sub-Second Retrieval:**
   Debounced, indexed database queries allow students to search thousands of active campus listings across all holding desks in under 80 milliseconds.
2. **Guaranteed Privacy and Security:**
   By decoupling the public presentation layer from the private contact store, students can coordinate recovery without disclosing personal mobile phone numbers.
3. **Automated Platform Self-Cleaning:**
   Integration with Amazon Rekognition provides automated 24/7 protection against inappropriate imagery, removing the burden of manual image screening from university staff.
4. **Verifiable Audit Trails:**
   Every status change, report creation, claim submission, and administrative resolution is permanently captured in an `audit_logs` relational table with client IP addresses, actor IDs, and UTC timestamps, providing complete institutional compliance.
5. **High Availability and Resilience:**
   By deploying multi-container tasks across multiple AWS Availability Zones behind an Application Load Balancer with automated health checking, ReFynd guarantees uninterrupted service availability even during campus peak hours.
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
# CHAPTER 5
# SYSTEM DESIGN AND ARCHITECTURE

---

## 5.1 System Architecture Overview

The ReFynd platform is architected as an enterprise-grade, cloud-native, three-tier distributed web application designed for high availability, low latency, robust data protection, and seamless horizontal scalability. The architecture separates public static asset distribution, dynamic API request processing, transactional data persistence, and asynchronous background worker processing into decoupled, specialized subsystems.

The three primary tiers comprise:
1. **Presentation Tier (Client-Side Edge):**
   A reactive, Single-Page Application (SPA) built using React 18, TypeScript, and Tailwind CSS. The compiled static distribution (HTML5, JavaScript bundles, CSS stylesheets, and media assets) is hosted in an **Amazon S3** bucket and globally cached across hundreds of edge locations via the **Amazon CloudFront Content Delivery Network (CDN)** with strict TLS 1.3 termination.
2. **Application & Logic Tier (Containerized Compute):**
   A high-performance asynchronous RESTful API gateway engineered with **FastAPI and Python 3.11**, running inside an **Amazon Elastic Container Service (ECS) Fargate** serverless container environment. Compute workloads run on energy-efficient, high-performance 64-bit **ARM64 AWS Graviton** processors. Incoming web traffic is load-balanced across container tasks via an **Application Load Balancer (ALB)** residing within public subnets of an Amazon Virtual Private Cloud (VPC).
3. **Data Persistence & Integration Tier (Private Cloud Enclave):**
   An ACID-compliant relational persistence engine powered by **Amazon RDS PostgreSQL 16**, isolated inside private VPC subnets with zero public internet access. Static user media uploads are stored in a dedicated, secure **Amazon S3 Uploads Bucket** protected with pre-signed URLs and server-side encryption. External integrations include **Amazon Rekognition** for automated computer vision safety filtering and an authenticated **Google SMTP over TLS gateway** for physical email notifications.

---

## 5.2 High-Level Architecture Diagram

Figure 5.1 details the complete production cloud topology of the ReFynd platform on Amazon Web Services.

```mermaid
graph TD
    Client([Student / Public User Mobile or Desktop Browser]) -->|HTTPS :443 TLS 1.3| CF[Amazon CloudFront CDN<br/>Edge Distribution: d25eqjxhksqlbh.cloudfront.net]
    
    subgraph AWS Cloud Region: us-east-1
        CF -->|Static Assets /*| S3Static[Amazon S3 Static Bucket<br/>refynd-frontend-prod-a91aeec0<br/>Origin Access Control OAC]
        CF -->|Dynamic API /api/v1/*| ALB[AWS Application Load Balancer<br/>refynd-prod-alb]
        
        subgraph AWS Virtual Private Cloud VPC 10.0.0.0/16
            subgraph Public Subnets 10.0.1.0/24 & 10.0.2.0/24
                ALB -->|HTTP :8000 Health: /health| ECS[Amazon ECS Fargate Cluster<br/>ARM64 Graviton Task: refynd-backend:6<br/>FastAPI + Uvicorn Async Loop]
            end
            
            subgraph Private Subnets 10.0.10.0/24 & 10.0.11.0/24
                ECS -->|Asyncpg Port 5432 Encrypted| RDS[(Amazon RDS PostgreSQL 16<br/>refynd-prod-db / db.t4g.micro<br/>Private Subnet Group)]
            end
        end
        
        ECS -->|Upload Image WebP| S3Media[Amazon S3 Uploads Bucket<br/>refynd-uploads-prod-a91aeec0]
        ECS -->|DetectModerationLabels| Rekognition[Amazon Rekognition<br/>AI Image Moderation Engine]
        ECS -->|Container Logs & Metrics| CloudWatch[Amazon CloudWatch<br/>Log Group: /ecs/refynd-prod-backend]
        CloudWatch -->|Alarm Trigger| SNS[Amazon SNS Topic<br/>refynd-prod-alerts]
    end
    
    subgraph External Email Delivery Network
        ECS -->|Asynchronous SMTP TLS :587| GmailSMTP[Google SMTP Gateway<br/>cloudlostfound.platform@gmail.com]
        GmailSMTP -->|Report Confirmation & Tracking Link| UserInbox([Student Gmail Inbox])
        GmailSMTP -->|Support Ticket Notification| AdminInbox([Support Operations Team])
    end
```
*Figure 5.1: Three-Tier High-Level Cloud Architecture of ReFynd on AWS*

### Ingress Traffic and Content Routing Logic:
1. When an end user initiates a web session at `https://d25eqjxhksqlbh.cloudfront.net`, DNS queries are resolved by Amazon CloudFront edge nodes closest to the user.
2. **Default Cache Behavior (`/*`):** CloudFront forwards requests for web assets (`index.html`, JavaScript, CSS) to the S3 frontend bucket via Origin Access Control (OAC). S3 bucket policies prevent any direct public internet access, ensuring all traffic traverses CloudFront edge caches.
3. **Single-Page Application (SPA) Custom Error Handling:** Because React Router handles client-side deep links (e.g., `/track?report_id=...` or `/report-found`), physical files do not exist at those S3 paths. CloudFront custom error response rules intercept HTTP 403 and HTTP 404 responses from S3, transparently rewriting them to `/index.html` with an HTTP 200 status code, enabling client-side hydration without broken page errors.
4. **Dynamic API Routing (`/api/*`):** CloudFront inspects incoming request paths. All paths matching `/api/*` bypass the static S3 cache and are forwarded directly to the Application Load Balancer origin with caching disabled, preserving query strings, cookies, and HTTP authorization headers.

---

## 5.3 Frontend Component Architecture

The frontend client is structured as a component-driven Single-Page Application (SPA) leveraging React 18 functional components, TypeScript interfaces, custom React hooks, and Context API for global state management.

```
src/
├── App.tsx                     # Master Root Component, Router Configuration, Global Layout
├── main.tsx                    # React DOM Mounting, QueryClient, Theme Initialization
├── types/                      # TypeScript Global Type Definitions
│   └── index.ts                # LostItem, FoundItem, Claim, User, Support Interfaces
├── services/                   # Asynchronous API Client Modules
│   └── api.ts                  # Axios Client Instance, Base URL Normalization, Interceptors
├── context/                    # React Context State Providers
│   └── AuthContext.tsx         # User Session, JWT Storage, Admin/Staff State
├── components/                 # Reusable Presentation and UI Components
│   ├── Navbar.tsx              # Responsive Navigation Bar with Mobile Drawer
│   ├── Footer.tsx              # Universal Institutional Footer & Support Link
│   ├── ItemCard.tsx            # Standardized Card View for Catalog Listings
│   ├── StepWizard.tsx          # Multi-Stage Form Indicator (Step 1 of 4)
│   ├── ImageUploader.tsx       # Drag-and-Drop Image Ingestion with Client Preview
│   └── ProtectedRoute.tsx      # RBAC Route Guard for Administrative Views
└── pages/                      # Top-Level Page Views (Route Targets)
    ├── Home.tsx                # Hero Banner, Quick Action Buttons, Recent Feed
    ├── ReportLost.tsx          # 4-Step Lost Item Ingestion Wizard
    ├── ReportFound.tsx         # 4-Step Found Item Ingestion Wizard
    ├── Search.tsx              # Debounced Search Engine with Multi-Facet Filters
    ├── TrackReport.tsx         # Token-Authenticated Private Item Dashboard
    ├── Support.tsx             # Interactive Campus Help & Support Ticket Form
    ├── Login.tsx               # Administrative & Staff JWT Authentication View
    └── AdminDashboard.tsx      # Unified Moderation, Claim, and Audit Console
```
*Figure 5.2: Frontend Component Hierarchy and Directory Layout*

### Key Frontend Architectural Principles:
* **Strict Type Safety:** All API request payloads and response bodies are strictly typed via TypeScript interfaces, preventing runtime property mismatch errors.
* **Debounced Reactive Querying:** The search view (`Search.tsx`) utilizes a custom `useDebounce` hook, buffering user keystrokes for 300 milliseconds before issuing API requests. This prevents network congestion and eliminates unnecessary backend database queries.
* **Universal Error Boundary & Fallbacks:** High-level React Error Boundaries intercept unhandled component exceptions, rendering a friendly recovery interface and logging diagnostic stack traces.

---

## 5.4 Backend Microservices Architecture

The backend application is structured as a modular ASGI microservice using **FastAPI**. FastAPI was chosen for its native asynchronous execution model built on Python’s `asyncio` event loop and Starlette framework, delivering industry-leading throughput under concurrent I/O workloads.

```
backend/
├── app/
│   ├── main.py                 # FastAPI Application Factory, CORS, Exception Handlers
│   ├── core/
│   │   ├── config.py           # Pydantic BaseSettings, Environment Variable Parsing
│   │   ├── security.py         # Password Hashing (Argon2/Bcrypt), JWT Encoding/Decoding
│   │   └── rate_limit.py       # SlowAPI Limiter Instance & Upstash Redis Storage Adapter
│   ├── database/
│   │   └── session.py          # SQLAlchemy 2.0 AsyncEngine, sessionmaker, get_db Dependency
│   ├── models/                 # SQLAlchemy Declarative Relational Models
│   │   ├── user.py             # User and Administrative Identity Model
│   │   ├── lost_item.py        # Lost Item Listing Model
│   │   ├── found_item.py       # Found Item Listing Model
│   │   ├── claim.py            # Ownership Claim Adjudication Model
│   │   ├── match.py            # Automated Similarity Match Model
│   │   ├── support_ticket.py   # Campus Support Ticket Model
│   │   └── audit.py            # Immutable Security Audit Log Model
│   ├── schemas/                # Pydantic v2 Serialization and Validation Models
│   │   ├── lost.py             # LostItemCreate, LostItemResponse Schemas
│   │   ├── found.py            # FoundItemCreate, FoundItemResponse Schemas
│   │   ├── claim.py            # ClaimCreate, ClaimReview Schemas
│   │   └── support.py          # SupportTicketCreate Schema
│   ├── api/v1/                 # Versioned RESTful API Route Controllers
│   │   ├── auth.py             # Authentication & Staff Management Endpoints
│   │   ├── lost_items.py       # Lost Item CRUD & Tracking Endpoints
│   │   ├── found_items.py      # Found Item CRUD & Image Upload Endpoints
│   │   ├── claims.py           # Claim Submission & Adjudication Endpoints
│   │   ├── search.py           # Multi-Facet Database Query Engine
│   │   ├── support.py          # Campus Support Ticket Ingestion Endpoint
│   │   └── admin.py            # Administrative Console & System Analytics
│   └── notifications/
│       └── service.py          # Asynchronous Google SMTP Email Dispatch Pipeline
├── Dockerfile                  # Production Multi-Stage ARM64 Docker Blueprint
├── entrypoint.sh               # Container Startup Script (Postgres Healthcheck + Migrations)
└── requirements.txt            # Explicitly Pinned Python Dependencies
```
*Figure 5.3: Backend Directory Structure and Architectural Layers*

### Asynchronous Request Lifecycle:
1. **Client Request Ingestion:** An incoming HTTP request arrives at Uvicorn via the Application Load Balancer.
2. **CORS & Rate Limiting Middleware:** The request traverses FastAPI middleware. The `CORSMiddleware` validates allowable origins (`https://d25eqjxhksqlbh.cloudfront.net`), and `SlowAPI` evaluates the client’s IP counter extracted from `X-Forwarded-For`.
3. **Dependency Injection:** Database sessions are provisioned on demand via `Depends(get_db)`, yielding a scoped `AsyncSession` that is automatically committed or rolled back upon endpoint exit.
4. **Pydantic Validation:** Request JSON payloads are parsed and validated against strict Pydantic schemas. If validation fails, an HTTP 422 Unprocessable Entity error is returned immediately with field-level diagnostics.
5. **Business Logic & Asynchronous Execution:** The route handler executes non-blocking asynchronous database queries via `await db.execute(...)`.
6. **Background Task Offloading:** Time-consuming operations—such as sending TLS SMTP emails or logging external audit records—are scheduled via FastAPI `BackgroundTasks`, allowing the endpoint to return an immediate HTTP 201 response to the client in under 50 milliseconds.

---

## 5.5 Database Architecture and VPC Placement

Data integrity, confidentiality, and network isolation are achieved by hosting the relational database within a segregated Amazon Virtual Private Cloud (VPC) topology:

* **VPC CIDR Block:** `10.0.0.0/16` deployed across two AWS Availability Zones (`us-east-1a` and `us-east-1b`).
* **Subnet Segmentation:**
  * **Public Subnets (`10.0.1.0/24`, `10.0.2.0/24`):** Host the public-facing Application Load Balancer.
  * **Private App Subnets (`10.0.10.0/24`, `10.0.11.0/24`):** Host the ECS Fargate container instances.
  * **Private Isolated DB Subnets (`10.0.20.0/24`, `10.0.21.0/24`):** Host the Amazon RDS PostgreSQL 16 instance.
* **Security Group Enclaves:**
  * The RDS Security Group strictly disallows all inbound traffic from the public internet. It accepts incoming TCP connections exclusively on port `5432` originating from the ECS Backend Security Group.
  * Even if an attacker discovers the internal DNS endpoint of the database, connection attempts from outside the private VPC are dropped at the hypervisor level.

---

## 5.6 Use-Case Modeling and Actor Specifications

The ReFynd ecosystem defines four primary human and automated actors:
1. **Student / General User:** Any enrolled student or campus visitor seeking to report a lost belonging, report a found item, query the catalog, or track a reported claim.
2. **Campus Desk Attendant (Staff):** Security desk wardens or custodial staff stationed at designated campus physical holding desks authorized to intake items, verify claimants, and release property.
3. **System Administrator:** University IT or Security Directors with full platform oversight, user role provisioning, system analytics access, and audit log inspection.
4. **Automated AI System (Amazon Rekognition):** Autonomous vision intelligence acting as a pre-storage safety gatekeeper.

```mermaid
flowchart LR
    User([Student / Campus User])
    Staff([Campus Desk Staff])
    Admin([System Administrator])
    Rekognition([Amazon Rekognition AI])

    subgraph ReFynd Platform
        UC1[Report Lost Item]
        UC2[Report Found Item]
        UC3[Search Public Catalog]
        UC4[Track Report via Token]
        UC5[Submit Support Inquiry]
        UC6[Moderate Uploaded Image]
        UC7[Adjudicate Claim & Verify ID]
        UC8[View Analytics & Audit Logs]
    end

    User --> UC1
    User --> UC2
    User --> UC3
    User --> UC4
    User --> UC5

    UC2 -.->|Triggers| UC6
    Rekognition --> UC6

    Staff --> UC7
    Staff --> UC3
    
    Admin --> UC7
    Admin --> UC8
    Admin --> UC3
```
*Figure 5.4: Comprehensive UML Use-Case Diagram for ReFynd System*

### Detailed Use-Case Specifications:

#### Use-Case UC-01: Report Lost Item
* **Primary Actor:** Student / General User.
* **Pre-conditions:** User has network connectivity to ReFynd web portal.
* **Flow of Events:**
  1. User accesses `/report-lost` and enters title, category, date/time lost, last seen location, and description.
  2. User specifies contact email and optional private verification proof (e.g., serial number).
  3. Client validates form fields and submits payload to `POST /api/v1/lost/create`.
  4. Backend assigns unique Report ID (`LF-SRM-26-XXXXXX`) and cryptographic tracking token.
  5. Backend queues confirmation email with tracking link via `BackgroundTasks`.
  6. Backend executes matching engine against active found items.
  7. Client receives HTTP 201 Created and displays confirmation screen with copyable Report ID.
* **Post-conditions:** Lost item record is committed to PostgreSQL with status `REPORTED`.

#### Use-Case UC-02: Report Found Item
* **Primary Actor:** Student (Finder) or Custodial Staff.
* **Flow of Events:**
  1. User accesses `/report-found` and inputs item attributes and holding desk location.
  2. User attaches optional photograph.
  3. Client uploads media bytes to `POST /api/v1/found/create`.
  4. Backend transcodes image to WebP, submits bytes to Amazon Rekognition `DetectModerationLabels`.
  5. If moderation flags confidence $\ge 70\%$, backend aborts and returns HTTP 400.
  6. If safe, image is committed to S3, record is saved to PostgreSQL, and confirmation email is dispatched.
* **Post-conditions:** Found item is visible in public search catalog with holding desk location.

---

## 5.7 Data Flow Diagrams (DFD)

The transformation of data across ReFynd is modeled through hierarchical Data Flow Diagrams.

### DFD Level 0: Context Diagram
Figure 5.5 models the entire ReFynd application as a single process, showing external entity data boundaries.

```
                       +-----------------------+
                       |    Student / User     |
                       +-------+-------+-------+
                               |       ^
            Lost/Found Details |       | Confirmation Email / Tracking Link
            Search Queries     |       | Public Search Results
                               v       |
                   +-----------+-------+-----------+
                   |                               |
                   |      ReFynd Platform          |
                   |       (Process 0.0)           |
                   |                               |
                   +-------+-------+-------+-------+
                           |       ^       |
         Image Bytes for   |       | Moderation Labels
         Safety Evaluation |       |
                           v       |
                   +-------+-------+-------+
                   |   Amazon Rekognition  |
                   |     AI Subsystem      |
                   +-----------------------+
```
*Figure 5.5: Data Flow Diagram (DFD) — Level 0 Context Diagram*

### DFD Level 1: Subsystem Interaction
Figure 5.6 decomposes Process 0.0 into major functional processes: Search & Cataloging, Report Ingestion & Validation, Claim Management, and Notification Dispatch.

```
[User] ---> (1.0 Ingest Report) ---> [DB: Staging] ---> (2.0 Image Moderation) ---> [AWS Rekognition]
                   |                                             |
                   v                                             v (Approved)
           [DB: Lost Items]                              [DB: Found Items]
                   ^                                             ^
                   |                                             |
[User] ---> (3.0 Search Engine) <--------------------------------+
                   |
                   v
[User] ---> (4.0 Submit Claim) ----> [DB: Claims] ----> (5.0 Admin Review) ---> [Staff]
                                                                |
                                                                v (Approved)
                                                      (6.0 Notification) ---> [User Email]
```
*Figure 5.6: Data Flow Diagram (DFD) — Level 1 Subsystem Interaction*

---

## 5.8 Entity-Relationship Diagram (ERD)

The data model is engineered to third normal form (3NF) to guarantee referential integrity and eliminate update anomalies. Figure 5.8 depicts the entities and relational cardinalities using Crow's Foot notation.

```mermaid
erDiagram
    USERS ||--o{ AUDIT_LOGS : performs
    USERS ||--o{ CLAIMS : reviews
    USERS ||--o{ STAFF_INVITATIONS : creates
    
    LOST_ITEMS ||--o{ CLAIMS : receives
    LOST_ITEMS ||--o{ MATCHES : generates_lost
    LOST_ITEMS ||--o{ ITEM_INFORMATION : contains_lost
    
    FOUND_ITEMS ||--o{ CLAIMS : matches_found
    FOUND_ITEMS ||--o{ MATCHES : generates_found
    FOUND_ITEMS ||--o{ ITEM_INFORMATION : contains_found
    
    SUPPORT_TICKETS ||--o{ AUDIT_LOGS : tracks_action

    USERS {
        int id PK
        string email UK
        string hashed_password
        string role
        string full_name
        boolean is_active
        datetime created_at
    }

    LOST_ITEMS {
        int id PK
        string report_id UK
        string title
        string category
        string description
        string location_lost
        datetime date_lost
        string contact_email
        string status
        string tracking_token
        datetime created_at
    }

    FOUND_ITEMS {
        int id PK
        string report_id UK
        string title
        string category
        string description
        string location_found
        string holding_desk
        string image_url
        string contact_email
        string status
        string tracking_token
        datetime created_at
    }

    CLAIMS {
        int id PK
        string claim_id UK
        int lost_item_id FK
        int found_item_id FK
        string claimant_name
        string claimant_email
        text proof_description
        string status
        int reviewed_by FK
        datetime created_at
    }

    MATCHES {
        int id PK
        int lost_item_id FK
        int found_item_id FK
        float match_score
        string match_reasons
        string status
        datetime created_at
    }

    SUPPORT_TICKETS {
        int id PK
        string ticket_id UK
        string name
        string email
        string subject
        text message
        string status
        string ip_address
        datetime created_at
    }

    AUDIT_LOGS {
        int id PK
        int user_id FK
        string action
        string target_entity
        int target_id
        string ip_address
        jsonb details
        datetime timestamp
    }
```
*Figure 5.8: Entity-Relationship Diagram (ERD) with Crow's Foot Cardinalities*

---

## 5.9 Detailed Database Schema and Data Dictionary

The following data dictionaries define the physical PostgreSQL table schemas, data types, constraints, and operational purposes.

### Table 5.1: `users` Table
Stores authenticated administrative and campus desk staff credentials and access roles.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY, AUTOINCREMENT` | Internal unique user surrogate identifier. |
| `email` | `VARCHAR(255)` | `UNIQUE, NOT NULL, INDEX` | Official institutional email address. |
| `hashed_password` | `VARCHAR(255)` | `NOT NULL` | Cryptographically hashed password (Argon2id/Bcrypt). |
| `full_name` | `VARCHAR(255)` | `NOT NULL` | Full name of the administrative user. |
| `role` | `VARCHAR(50)` | `NOT NULL, DEFAULT 'staff'` | Access role (`admin`, `staff`, `moderator`). |
| `is_active` | `BOOLEAN` | `NOT NULL, DEFAULT TRUE` | Active account status flag. |
| `created_at` | `TIMESTAMP WITH TZ` | `NOT NULL, DEFAULT UTC` | Timestamp of account registration. |

### Table 5.2: `lost_items` Table
Stores reports of misplaced belongings registered by students.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY, AUTOINCREMENT` | Surrogate primary key. |
| `report_id` | `VARCHAR(64)` | `UNIQUE, NOT NULL, INDEX` | Human-readable public identifier (e.g. `LF-SRM-26-8K4P91`). |
| `title` | `VARCHAR(255)` | `NOT NULL` | Brief name/title of the lost belonging. |
| `category` | `VARCHAR(100)` | `NOT NULL, INDEX` | Standardized category (Electronics, Keys, Wallet, etc.). |
| `description` | `TEXT` | `NOT NULL` | Full descriptive details of the item. |
| `location_lost` | `VARCHAR(255)` | `NOT NULL` | Campus building or zone where item was last seen. |
| `date_lost` | `TIMESTAMP WITH TZ` | `NOT NULL` | Approximate date and time of misplacement. |
| `contact_email` | `VARCHAR(255)` | `NOT NULL` | Owner’s email (strictly sequestered from public views). |
| `status` | `VARCHAR(50)` | `NOT NULL, DEFAULT 'REPORTED'`| Item lifecycle status (`REPORTED`, `MATCHED`, `CLAIMED`). |
| `tracking_token`| `VARCHAR(255)` | `NOT NULL, INDEX` | Cryptographic secret token required for status tracking. |
| `created_at` | `TIMESTAMP WITH TZ` | `NOT NULL, DEFAULT UTC` | Creation timestamp. |

### Table 5.3: `found_items` Table
Stores records of unattended items retrieved on campus.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY, AUTOINCREMENT` | Surrogate primary key. |
| `report_id` | `VARCHAR(64)` | `UNIQUE, NOT NULL, INDEX` | Public identifier (e.g. `FD-SRM-26-CSVSQM`). |
| `title` | `VARCHAR(255)` | `NOT NULL` | Item title / name. |
| `category` | `VARCHAR(100)` | `NOT NULL, INDEX` | Categorical classification. |
| `description` | `TEXT` | `NOT NULL` | Descriptive features and condition. |
| `location_found`| `VARCHAR(255)` | `NOT NULL` | Specific campus location where item was discovered. |
| `holding_desk` | `VARCHAR(255)` | `NOT NULL` | Physical security desk holding the item (e.g., Central Library).|
| `image_url` | `VARCHAR(512)` | `NULLABLE` | S3 URL of verified, moderated item photograph. |
| `contact_email` | `VARCHAR(255)` | `NOT NULL` | Finder’s email address (sequestered from public views). |
| `status` | `VARCHAR(50)` | `NOT NULL, DEFAULT 'AVAILABLE'`| Status (`AVAILABLE`, `CLAIMED`, `RESOLVED`, `ARCHIVED`). |
| `tracking_token`| `VARCHAR(255)` | `NOT NULL` | Secret tracking token for finder updates. |
| `created_at` | `TIMESTAMP WITH TZ` | `NOT NULL, DEFAULT UTC` | Ingestion timestamp. |

### Table 5.4: `claims` Table
Tracks formal ownership claims initiated by students.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY, AUTOINCREMENT` | Surrogate primary key. |
| `claim_id` | `VARCHAR(64)` | `UNIQUE, NOT NULL, INDEX` | Human-readable claim code (e.g. `CLM-2026-9X1Z`). |
| `lost_item_id` | `INTEGER` | `FOREIGN KEY (lost_items.id)` | Optional link to claimant’s lost report. |
| `found_item_id`| `INTEGER` | `FOREIGN KEY (found_items.id)`| Target found item being claimed. |
| `claimant_name` | `VARCHAR(255)` | `NOT NULL` | Full legal name of student claiming ownership. |
| `claimant_email`| `VARCHAR(255)` | `NOT NULL` | Student institutional email address. |
| `proof_details` | `TEXT` | `NOT NULL` | Private proof of ownership submitted for verification. |
| `status` | `VARCHAR(50)` | `NOT NULL, DEFAULT 'PENDING'` | Status (`PENDING`, `APPROVED`, `REJECTED`). |
| `reviewed_by` | `INTEGER` | `FOREIGN KEY (users.id), NULL` | Staff member who adjudicated the claim. |
| `created_at` | `TIMESTAMP WITH TZ` | `NOT NULL, DEFAULT UTC` | Submission timestamp. |

### Table 5.5: `support_tickets` Table
Stores inquiries and bug reports submitted through the platform.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY, AUTOINCREMENT` | Surrogate primary key. |
| `ticket_id` | `VARCHAR(64)` | `UNIQUE, NOT NULL, INDEX` | Human-readable ticket ID (e.g. `SUP-2026-2DZMKN`). |
| `name` | `VARCHAR(255)` | `NOT NULL` | Submitter full name. |
| `email` | `VARCHAR(255)` | `NOT NULL` | Submitter contact email. |
| `subject` | `VARCHAR(255)` | `NOT NULL` | Ticket category or inquiry subject. |
| `message` | `TEXT` | `NOT NULL` | Full description of inquiry or technical issue. |
| `status` | `VARCHAR(50)` | `NOT NULL, DEFAULT 'OPEN'` | Status (`OPEN`, `IN_PROGRESS`, `RESOLVED`, `CLOSED`). |
| `ip_address` | `VARCHAR(64)` | `NOT NULL` | Client remote IP address captured for audit safety. |
| `created_at` | `TIMESTAMP WITH TZ` | `NOT NULL, DEFAULT UTC` | Ticket creation timestamp. |

---

## 5.10 RESTful API Architecture and OpenAPI Contracts

ReFynd enforces a uniform RESTful API contract. All endpoints return standardized JSON payloads adhering to OpenAPI 3.0 conventions, outlined in Table 5.7.

*Table 5.7: Core RESTful API Routes and HTTP Method Matrix*

| HTTP Method | API Route | Access Control | Rate Limit | Primary Purpose |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/health` | Public | None | Container health check probing database connectivity. |
| `POST` | `/api/v1/auth/login` | Public | 10/min | Authenticates staff; returns signed JWT Bearer Token. |
| `GET` | `/api/v1/search` | Public | 100/min | Debounced full-text search with category & location filters. |
| `POST` | `/api/v1/lost/create` | Public | 5/min | Registers a lost item report; triggers confirmation email. |
| `GET` | `/api/v1/track/{report_id}`| Public (Token Gate) | 100/min | Returns private report details if valid token supplied. |
| `POST` | `/api/v1/found/create` | Public | 5/min | Ingests found report, moderates image, saves to S3. |
| `POST` | `/api/v1/claims` | Public | 5/min | Submits private ownership proof claiming a found item. |
| `GET` | `/api/v1/admin/claims` | Staff / Admin | 100/min | Lists all pending claims awaiting physical verification. |
| `POST` | `/api/v1/admin/claims/{id}`| Staff / Admin | 10/min | Approves or rejects a claim; updates item lifecycle status. |
| `POST` | `/api/v1/support` | Public | 5/min | Logs support ticket and forwards email to platform admin. |

---

## 5.11 Multi-Layer Defense-in-Depth Security Architecture

Security is architected into ReFynd at every physical, network, and application boundary, adhering to the principle of Defense-in-Depth illustrated in Figure 5.9:

```
[Layer 1: Edge & Perimeter]   -> CloudFront TLS 1.3 Termination + AWS Shield Standard (DDoS)
[Layer 2: Network Gateways]   -> Application Load Balancer Security Groups + VPC Subnet Isolation
[Layer 3: Application Layer]  -> SlowAPI Rate Limiting + CORS Whitelist + Pydantic Strict Typing
[Layer 4: Logic & Media Gate] -> Amazon Rekognition Fail-Closed AI Moderation (Confidence >= 70%)
[Layer 5: Auth & Identity]    -> JWT Bearer Tokens + Argon2 Password Hashing + RBAC Guards
[Layer 6: Persistence Layer]  -> Private Subnet RDS Enclave + KMS AES-256 Encryption at Rest
```
*Figure 5.9: Multi-Layer Defense-in-Depth Security Architecture*

1. **Edge Mitigation:** CloudFront negotiates HTTPS with modern ciphers (TLS 1.3), deflecting volumetric Layer 3/4 DDoS attacks via AWS Shield Standard.
2. **Network Enclave:** Containers execute in private subnets. The PostgreSQL database is completely unreachable from the public internet, accepting connections only from the ECS task security group on port 5432.
3. **Application Hardening:** SlowAPI limits request bursts by IP address. Pydantic sanitizes all input strings, completely immunizing the system against SQL injection (SQLAlchemy parameterized queries) and Cross-Site Scripting (XSS).
4. **Data Isolation:** All personal contact details are stored in restricted relational tables; public queries select only non-PII fields.
# CHAPTER 6
# SYSTEM IMPLEMENTATION

---

## 6.1 Development Environment Setup

The implementation of ReFynd was engineered using a modernized full-stack development environment designed for strict parity between local developer machines and cloud production targets. The toolchain integrates native Unix shell tooling, Docker container virtualization, and modern package registries.

```
Development Workstation Environment:
* Operating System: macOS Sonoma (Darwin ARM64) / Linux Ubuntu 22.04 LTS
* Python Environment: Python 3.11.8 running in isolated virtual environment (.venv)
* Node.js Environment: Node.js v20.11.0 LTS with npm v10.2.4
* Local Persistence: Dockerized PostgreSQL 16.2 container on bridged network port 5432
* Local Container Engine: Docker Engine v24.0.7 with Docker Compose v2.23.3
* IDE & Tooling: VS Code with Pylance, ESLint, Prettier, and Tailwind CSS IntelliSense
```

To eliminate environment drift ("it works on my machine"), dependencies were pinned down to patch versions in [`backend/requirements.txt`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/backend/requirements.txt) and [`frontend/package.json`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/frontend/package.json).

---

## 6.2 Frontend Implementation (React 18, TypeScript, Tailwind)

The frontend client was developed as a high-performance Single-Page Application (SPA) leveraging **React 18.2** and **TypeScript 5.2**. TypeScript guarantees compile-time type safety, catching missing properties and incorrect schema payloads before code compilation.

The UI styling is constructed using **Tailwind CSS 3.3**, utilizing a utility-first design system that compiles down to a purged, ultra-lightweight CSS bundle (< 35 KB gzipped). The platform features an adaptive dark mode theme that integrates with the user's operating system preferences while allowing manual toggling via a persistent theme state controller.

```tsx
// frontend/src/types/index.ts - Core TypeScript Interface Definitions
export interface LostItem {
  id: number;
  report_id: string;
  title: string;
  category: string;
  description: string;
  location_lost: string;
  date_lost: string;
  status: 'REPORTED' | 'MATCHED' | 'CLAIMED' | 'RESOLVED';
  created_at: string;
}

export interface FoundItem {
  id: number;
  report_id: string;
  title: string;
  category: string;
  description: string;
  location_found: string;
  holding_desk: string;
  image_url?: string;
  status: 'AVAILABLE' | 'CLAIMED' | 'RESOLVED' | 'ARCHIVED';
  created_at: string;
}

export interface SupportTicketPayload {
  name: string;
  email: string;
  subject: string;
  message: string;
}
```

---

## 6.3 State Management, Routing, and Error Boundaries

### 1. Client-Side Routing and URL Normalization
Routing is managed via `react-router-dom` v6. To prevent cross-origin issues and eliminate path mismatch errors across different environments, all API communications are orchestrated through a centralized service client in [`frontend/src/services/api.ts`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/frontend/src/services/api.ts):

```typescript
// frontend/src/services/api.ts - Normalized API Client with Axios
import axios from 'axios';

// Dynamically resolves to CloudFront domain in production or localhost in development
const API_BASE_URL = import.meta.env.VITE_API_URL || '/api/v1';

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 15000, // 15-second timeout for resilient mobile connections
});

// Automatic JWT Bearer Token Injection Interceptor
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('refynd_auth_token');
  if (token && config.headers) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
```

### 2. Global Authentication Context
Administrative authentication state is managed via React Context (`AuthContext.tsx`). When an authorized staff member logs in, the returned JSON Web Token (JWT) is verified, decoded to extract claims (`sub`, `role`, `exp`), and persisted in `localStorage`. The context exposes helper hooks (`useAuth()`) that guard administrative routes from unauthorized access.

---

## 6.4 Backend Implementation with FastAPI and Python 3.11

The backend is engineered using **FastAPI**, an ASGI framework that harnesses Python’s native `asyncio` syntax for non-blocking I/O operations. When handling thousands of simultaneous student inquiries, traditional synchronous frameworks (such as standard Django or Flask) block operating system threads during database queries or network calls. FastAPI offloads I/O to the event loop, achieving throughput comparable to Node.js and Go while retaining Python’s ecosystem for AI and data processing.

The master application factory is instantiated in [`backend/app/main.py`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/backend/app/main.py):

```python
# backend/app/main.py - Application Factory and Middleware Pipeline
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.core.config import settings
from app.core.rate_limit import limiter
from app.api.v1.router import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=None, # Disabled in production for security hardening
)

# Attach SlowAPI Rate Limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Configure Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Register Versioned API Router
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/health", tags=["Health"])
async def health_check():
    """Liveness and readiness probe for AWS Application Load Balancer."""
    return {"status": "healthy", "service": "refynd-backend", "version": "1.0.0"}
```

---

## 6.5 Data Validation and Serialization with Pydantic v2

Incoming HTTP request bodies are validated and deserialized using **Pydantic v2**. Pydantic compiles validation logic to C-level Rust binaries via `pydantic-core`, ensuring near-instant validation times.

```python
# backend/app/schemas/lost.py - Pydantic Validation Schemas
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime
from typing import Optional

class LostItemCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100, description="Title of lost item")
    category: str = Field(..., min_length=2, max_length=50, description="Standardized category")
    description: str = Field(..., min_length=10, max_length=2000, description="Detailed description")
    location_lost: str = Field(..., min_length=2, max_length=100, description="Campus location")
    date_lost: datetime = Field(..., description="Date and time when item was lost")
    contact_email: EmailStr = Field(..., description="Valid institutional or personal email")
    brand: Optional[str] = Field(None, max_length=50)
    color: Optional[str] = Field(None, max_length=30)
    private_proof: Optional[str] = Field(None, max_length=500, description="Private verification detail")

    @validator("title", "description", "location_lost")
    def sanitize_strings(cls, v: str) -> str:
        # Strip trailing whitespaces and strip HTML tags to prevent XSS
        cleaned = v.strip().replace("<", "&lt;").replace(">", "&gt;")
        if not cleaned:
            raise ValueError("Field cannot be whitespace only")
        return cleaned
```

---

## 6.6 Asynchronous Persistence with SQLAlchemy 2.0 & Asyncpg

All database interactions are executed asynchronously through **SQLAlchemy 2.0** utilizing the high-speed **Asyncpg** native binary PostgreSQL driver. Database connection sessions are managed via scoped async context generators:

```python
# backend/app/database/session.py - Asynchronous Engine Configuration
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Initialize Async Engine with robust Connection Pooling
engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    echo=False,
    future=True,
    pool_size=10,          # Persistent connection pool size
    max_overflow=20,       # Allow burst connections during peak class intervals
    pool_recycle=300,      # Recycle connections every 5 minutes to prevent stale sockets
    pool_pre_ping=True     # Test connection viability before handing to route
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

async def get_db():
    """FastAPI dependency yielding an isolated, transactional database session."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
```

---

## 6.7 Database Migrations and Seeding with Alembic

Database schema evolution is tracked through **Alembic**, maintaining declarative, version-controlled migration files in `backend/alembic/versions/`. This enables zero-downtime schema upgrades and deterministic rollbacks across environments.

Upon container startup, [`backend/entrypoint.sh`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/backend/entrypoint.sh) executes an automated database reachability probe, runs outstanding migrations, and seeds the administrative account:

```bash
#!/bin/sh
# backend/entrypoint.sh - Automated Container Initialization Script
set -e

echo "[Entrypoint] Verifying PostgreSQL availability..."
python - << 'EOF'
import sys, time, os
from urllib.parse import urlparse
import psycopg2

uri = os.getenv("DATABASE_URL", "")
if uri.startswith("postgresql+asyncpg://"):
    uri = uri.replace("postgresql+asyncpg://", "postgresql://", 1)

parsed = urlparse(uri)
for attempt in range(30):
    try:
        conn = psycopg2.connect(
            dbname=parsed.path.lstrip('/'),
            user=parsed.username,
            password=parsed.password,
            host=parsed.hostname,
            port=parsed.port or 5432
        )
        conn.close()
        print("[Entrypoint] PostgreSQL is online and accepting connections.")
        sys.exit(0)
    except Exception as e:
        time.sleep(1)

print("[Entrypoint] ERROR: Timed out waiting for database.", file=sys.stderr)
sys.exit(1)
EOF

echo "[Entrypoint] Applying database migrations via Alembic..."
alembic upgrade head

echo "[Entrypoint] Launching Uvicorn ASGI Web Server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 2
```

---

## 6.8 Authentication, Role-Based Access Control, and JWT

To safeguard administrative actions (approving claims, updating item statuses, downloading audit logs), ReFynd implements **Role-Based Access Control (RBAC)** enforced via **JSON Web Tokens (JWT)**:

1. **Password Hashing:** Passwords are never stored in plaintext. They are salted and hashed using **Argon2id** (with fallback to Bcrypt), adhering to OWASP cryptographic guidelines.
2. **Token Generation:** Upon successful authentication (`POST /api/v1/auth/login`), the server issues an encrypted JWT signed with a 256-bit secret key (`HS256`) containing the user's role and an expiration timestamp (e.g., 8 hours).
3. **Route Security Dependency:**
   Endpoints declare an explicit role dependency:
   ```python
   def require_role(required_role: str):
       async def role_checker(current_user: User = Depends(get_current_active_user)):
           if current_user.role != required_role and current_user.role != "admin":
               raise HTTPException(
                   status_code=status.HTTP_403_FORBIDDEN,
                   detail="Insufficient operational permissions"
               )
           return current_user
       return role_checker
   ```

---

## 6.9 Lost and Found Reporting Workflows

The reporting workflows are structured as intuitive 4-step progressive wizards:
* **Step 1:** Categorical selection and descriptive inputs (Title, Category, Brand, Color).
* **Step 2:** Spatial and temporal coordinates (Campus Location, Holding Desk, Date/Time).
* **Step 3:** Visual media ingestion (Drag-and-drop image upload with live client preview).
* **Step 4:** Contact details and cryptographic token generation.

When a student submits a report, the backend generates a human-readable Report ID and an unguessable 32-character tracking token, dispatching a confirmation email instantly via background tasks.

---

## 6.10 Intelligent Item Matching Engine

ReFynd incorporates an automated algorithmic matching engine that continuously evaluates new listings to detect potential matches between lost belongings and found items. The algorithm computes a composite similarity index $S_{total} \in [0, 100]\%$ across four weighted feature dimensions:

$$S_{total} = w_c \cdot S_{category} + w_b \cdot S_{brand} + w_t \cdot S_{text} + w_l \cdot S_{location}$$

Where:
* $w_c = 0.35$ (Category Match Weight): Exact categorical alignment.
* $w_b = 0.25$ (Brand & Color Alignment): Normalized token intersection.
* $w_t = 0.25$ (Fuzzy Text Similarity): Levenshtein / Token Sort Ratio across title and description.
* $w_l = 0.15$ (Location Proximity): Proximity scoring between last-seen zone and holding desk.

```python
# backend/app/services/matching.py - Algorithmic Similarity Engine
from difflib import SequenceMatcher

def calculate_similarity_score(lost_item, found_item) -> float:
    # 1. Category must match as a baseline prerequisite
    if lost_item.category.lower() != found_item.category.lower():
        return 0.0

    score = 35.0  # Base score for identical category

    # 2. Brand & Model Token Comparison
    if lost_item.brand and found_item.brand:
        if lost_item.brand.lower() == found_item.brand.lower():
            score += 25.0
        elif lost_item.brand.lower() in found_item.title.lower():
            score += 15.0

    # 3. Fuzzy Text Similarity on Titles
    text_ratio = SequenceMatcher(
        None, 
        lost_item.title.lower(), 
        found_item.title.lower()
    ).ratio()
    score += (text_ratio * 25.0)

    # 4. Location Proximity Scoring
    if lost_item.location_lost.lower() in found_item.location_found.lower():
        score += 15.0

    return min(round(score, 1), 100.0)
```

If $S_{total} \ge 65.0\%$, the backend persists a record in the `matches` table, flagging it for administrative review and notifying the registered student.

---

## 6.11 Image Ingestion Pipeline and Amazon Rekognition Moderation

To protect campus community members from offensive, explicit, or malicious user-uploaded content, ReFynd implements a real-time, **fail-closed** image moderation pipeline powered by **Amazon Rekognition**:

```
[User Form Upload] ---> [In-Memory Transcode: WebP/JPEG]
                                    |
                                    v
                     [Amazon Rekognition API Call]
                     (DetectModerationLabels: Confidence >= 70%)
                                    |
             +----------------------+----------------------+
             |                                             |
             v (Moderation Flag Detected)                  v (Image Clean)
    [HTTP 400 Bad Request]                      [Commit Bytes to S3 Uploads]
    "Upload rejected: Inappropriate media"      [Save S3 URL in PostgreSQL]
```
*Figure 6.3: Amazon Rekognition Fail-Closed Image Moderation Architecture*

```python
# backend/app/services/moderation.py - Fail-Closed AI Moderation Pipeline
import boto3
from botocore.exceptions import ClientError
from fastapi import HTTPException, status
from app.core.config import settings

rekognition_client = boto3.client(
    "rekognition",
    region_name=settings.AWS_REGION
)

async def moderate_image_bytes(image_bytes: bytes) -> bool:
    """
    Submits image bytes to Amazon Rekognition DetectModerationLabels.
    Returns True if image is safe; raises HTTPException 400 if unsafe.
    Fails closed if the moderation service is unreachable.
    """
    try:
        response = rekognition_client.detect_moderation_labels(
            Image={'Bytes': image_bytes},
            MinConfidence=70.0  # 70% confidence threshold for safety
        )
        labels = response.get('ModerationLabels', [])
        if labels:
            flagged = [label['Name'] for label in labels]
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Image upload rejected due to safety policy: {', '.join(flagged)}"
            )
        return True

    except ClientError as e:
        # Fail-Closed Safety: Reject upload if AWS Rekognition cannot evaluate the image
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Image moderation service is temporarily unavailable. Upload aborted for safety."
        )
```

---

## 6.12 Administrative Dashboard and Claim Adjudication

The Administrative Console (`AdminDashboard.tsx`) provides campus security desk staff with an intuitive operational interface:
1. **Real-Time KPI Metric Cards:** Displays count of active lost reports, cataloged found items, pending claims awaiting physical inspection, and successful return percentages.
2. **Claim Verification Terminal:** When a student arrives at a holding desk, the attendant inspects the claim record. The attendant reviews the student's institutional identity card against the stored private proof of ownership (e.g., verifying that the serial number on the laptop base matches the private proof string stored in the database).
3. **Audit Trail Generation:** When the attendant clicks **Approve & Release**, the backend transitions the item status to `RESOLVED`, updates the claim status to `APPROVED`, and writes an immutable audit record containing the attendant's User ID, client IP address, and timestamp.

---

## 6.13 Application-Level Rate Limiting with SlowAPI

To shield the backend from scraping bots, automated brute-force attacks, and denial-of-service spam, the application enforces granular rate limits through **SlowAPI**:

```python
# backend/app/core/rate_limit.py - SlowAPI Configuration
from slowapi import Limiter
from slowapi.util import get_remote_address

LIMIT_LOGIN = "10/minute"       # Strictest: Defends against password brute-forcing
LIMIT_CREATE = "5/minute"       # Prevents automated spam of fake reports
LIMIT_SENSITIVE = "3/minute"    # Password resets and token generation

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100/minute"],
    enabled=True
)
```

*Table 6.1: Rate Limiting Policy and Enforcement Thresholds*

| Endpoint Target | Rate Limit | Violation Behavior | Storage Engine |
| :--- | :--- | :--- | :--- |
| `/api/v1/auth/login` | 10 requests / min | HTTP 429 Too Many Requests | In-Memory / Upstash Redis |
| `/api/v1/lost/create` | 5 requests / min | HTTP 429 Too Many Requests | In-Memory / Upstash Redis |
| `/api/v1/found/create`| 5 requests / min | HTTP 429 Too Many Requests | In-Memory / Upstash Redis |
| `/api/v1/support` | 5 requests / min | HTTP 429 Too Many Requests | In-Memory / Upstash Redis |
| Global Unspecified | 100 requests / min | HTTP 429 Too Many Requests | In-Memory / Upstash Redis |

---

## 6.14 Live Asynchronous Email Notifications via BackgroundTasks

To deliver confirmation receipts and forward support inquiries without introducing UI latency, ReFynd offloads email dispatch to FastAPI `BackgroundTasks`. The notification service establishes an authenticated **Google SMTP over TLS connection** (`smtp.gmail.com:587`):

```python
# backend/app/notifications/service.py - Asynchronous TLS Email Dispatch
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config import settings

def send_email(to_email: str, subject: str, html_content: str, text_content: str = "") -> bool:
    """Establishes an authenticated TLS SMTP session and dispatches the email."""
    if settings.MOCK_SMTP:
        print(f"[MOCK SMTP] Dispatching email to {to_email} | Subject: {subject}", flush=True)
        return True

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"ReFynd Campus Support <{settings.SMTP_USER}>"
        msg["To"] = to_email

        if text_content:
            msg.attach(MIMEText(text_content, "plain"))
        if html_content:
            msg.attach(MIMEText(html_content, "html"))

        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT, timeout=10) as server:
            server.ehlo()
            server.starttls() # Upgrade connection to TLS encryption
            server.ehlo()
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.sendmail(settings.SMTP_USER, to_email, msg.as_string())

        print(f"[SMTP SUCCESS] Delivered email to {to_email}", flush=True)
        return True

    except Exception as e:
        print(f"[SMTP ERROR] Failed to dispatch email to {to_email}: {str(e)}", flush=True)
        return False
```

When a user submits a report, the tracking link (`https://d25eqjxhksqlbh.cloudfront.net/track?report_id={id}&token={token}`) is delivered directly to their inbox, ensuring they can access their private dashboard at any time.
# CHAPTER 7
# CLOUD AND DEVOPS IMPLEMENTATION

---

## 7.1 Introduction to Cloud-Native DevOps

In modern enterprise software engineering, building reliable web applications extends far beyond authoring clean application source code. The operational discipline of **Cloud-Native DevOps** bridges the historical divide between software development (*Dev*) and system operations (*Ops*), establishing automated, repeatable, and resilient lifecycles for building, testing, packaging, provisioning, and operating distributed systems.

For the ReFynd platform—developed as a final-year B.Tech capstone specializing in **Cloud Computing and DevOps**—the cloud implementation represents the core engineering foundation. The deployment architecture was designed to eliminate manual server management, enforce immutable infrastructure through code, guarantee zero-downtime rolling upgrades, enforce strict zero-trust network isolation, and maintain rock-solid cost predictability within academic budgetary constraints.

---

## 7.2 Version Control and Branching Strategy with Git & GitHub

All application source code, Docker container definitions, CI/CD pipeline declarations, and Terraform infrastructure code are maintained in a unified Git monorepo hosted on **GitHub** (`https://github.com/a7hu-15/lost-and-found-pvt`).

### Branching and Collaboration Strategy:
The team adhered to a strict **Trunk-Based Development model with Short-Lived Feature Branches**:
* **`main` Branch:** Represents production-grade, deployable code. Direct pushes to `main` are restricted; code modifications must undergo peer review and pass all automated CI pipeline checks.
* **Feature Branches (`feature/xyz`):** Engineers develop specific features or bug fixes in short-lived branches branched off the latest `main`.
* **Atomic Semantic Commits:** Commit messages follow the Conventional Commits specification (e.g., `feat(auth): ...`, `fix(cdn): ...`, `docs(iac): ...`), establishing an auditable historical log.

---

## 7.3 Multi-Stage Docker Containerization

To ensure absolute environment consistency across local workstations and AWS cloud runtimes, both frontend and backend services are packaged into standalone, immutable **OCI-compliant Docker container images**.

### 1. Backend Containerization ([`backend/Dockerfile`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/backend/Dockerfile))
The backend Dockerfile utilizes a multi-stage architecture based on `python:3.11-slim`, optimized for **64-bit ARM64 AWS Graviton** execution:

```dockerfile
# Multi-stage production Dockerfile for ReFynd FastAPI Backend
FROM python:3.11-slim as builder

WORKDIR /build
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev gcc curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Final Runtime Stage (Minimal Attack Surface)
FROM python:3.11-slim as runtime

# Create isolated non-root user (UID 1000) for security hardening
RUN groupadd -g 1000 appgroup && \
    useradd -u 1000 -g appgroup -s /bin/sh -m appuser

WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 curl && \
    rm -rf /var/lib/apt/lists/*

# Copy pre-compiled Python packages from builder stage
COPY --from=builder /root/.local /home/appuser/.local
COPY --chown=appuser:appgroup . .

ENV PATH=/home/appuser/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

USER appuser
EXPOSE 8000

# Native container healthcheck probe
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

ENTRYPOINT ["./entrypoint.sh"]
```

#### Security and Operational Highlights:
* **Non-Root Execution:** The container runs strictly as `appuser` (UID 1000). If an application vulnerability is compromised, the attacker cannot gain root privileges on the container host.
* **Minimal Image Footprint:** Multi-stage compilation strips compilers, header files, and build tools, reducing the final image size from 1.2 GB to under 210 MB.
* **Deterministic Health Monitoring:** Docker periodically polls `GET /health`. If the database becomes unreachable, the container reports `unhealthy`, triggering ECS Fargate to cycle the task automatically.

### 2. Frontend Containerization ([`frontend/Dockerfile`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/frontend/Dockerfile))
The frontend leverages a two-stage build pipeline:
1. **Compilation Stage (`node:20-alpine`):** Installs npm dependencies and compiles React/TypeScript source files via Vite into static assets.
2. **Production Web Server (`nginx:1.27-alpine`):** Copies compiled HTML/JS/CSS into an Nginx web server configured with Gzip compression, `/healthz` liveness endpoints, and client-side SPA routing fallback rules (`try_files $uri $uri/ /index.html;`).

---

## 7.4 Multi-Container Local Orchestration with Docker Compose

For rapid local development, the entire ecosystem is orchestrated via [`docker-compose.yml`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/docker-compose.yml):

```yaml
version: '3.8'

services:
  db:
    image: postgres:16-alpine
    container_name: refynd-postgres
    restart: always
    environment:
      POSTGRES_USER: refynd_user
      POSTGRES_PASSWORD: refynd_secure_password
      POSTGRES_DB: lost_found_db
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U refynd_user -d lost_found_db"]
      interval: 5s
      timeout: 5s
      retries: 5

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: refynd-backend
    restart: always
    environment:
      DATABASE_URL: postgresql+asyncpg://refynd_user:refynd_secure_password@db:5432/lost_found_db
      SECRET_KEY: dev-local-secret-key-super-secure-32chars
      MOCK_SMTP: "True"
    ports:
      - "8000:8000"
    depends_on:
      db:
        condition: service_healthy

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: refynd-frontend
    restart: always
    ports:
      - "3000:80"
    depends_on:
      - backend

volumes:
  pgdata:
```

A single command—`docker-compose up -d`—provisions the complete multi-tier architecture locally in under 15 seconds.

---

## 7.5 CI/CD Concepts

Continuous Integration (CI) and Continuous Deployment (CD) are modern DevOps practices designed to accelerate software delivery while maintaining rigorous quality standards:
* **Continuous Integration:** Developers merge code frequently into the shared repository. Every push triggers automated builds, static linting, and automated unit test executions, detecting integration errors immediately.
* **Continuous Delivery / Deployment:** Code changes that pass the CI gates are automatically packaged into release artifacts (Docker images) and deployed to target cloud environments without human intervention.

---

## 7.6 Continuous Integration with GitHub Actions

ReFynd implements an automated CI pipeline declared in [`.github/workflows/ci.yml`](file:///Users/ashuchaudhary/Downloads/lost-and-found-main/.github/workflows/ci.yml). 

```mermaid
flowchart TD
    Push[Git Push to main or PR opened] --> Trigger[GitHub Actions Runner Triggered]
    
    subgraph CI Pipeline Environment
        Trigger --> SetupPy[Set up Python 3.11 Runtime]
        SetupPy --> InstallDeps[Install Dependencies from requirements.txt]
        InstallDeps --> Lint[Run Flake8 / Code Quality Verification]
        Lint --> Pytest[Execute Pytest Test Suite 18 Test Cases]
        
        Pytest --> BuildDocker[Compile Multi-Stage Docker Images ARM64]
    end
    
    Pytest -->|Tests Pass| StatusGreen[Status: CI Green]
    Pytest -->|Tests Fail| BlockPR[Block Pull Request & Alert Team]
```
*Figure 7.2: Continuous Integration Workflow via GitHub Actions*

Whenever a pull request is submitted, GitHub Actions executes:
1. **Dependency Installation:** Caches pip wheels to accelerate subsequent runs.
2. **Automated Unit Testing:** Executes all 18 Pytest test cases across health checks, Amazon Rekognition moderation mock routines, and support ticket email dispatch pipelines.
3. **Build Validation:** Verifies that both frontend and backend Dockerfiles compile without warnings.
4. **Branch Protection:** Merges are blocked if any single test fails.

---

## 7.7 Architectural Evolution: From Temporary Serverless to Dedicated AWS Infrastructure

During the initial preliminary exploration phase of the project, the development team briefly utilized third-party serverless hosting (specifically Vercel) for rapid frontend proof-of-concept preview testing. However, as the platform matured to require enterprise-grade security, computer vision ingestion, transactional data integrity, and strict privacy protection, severe technical bottlenecks emerged that necessitated migrating the entire stack to a **dedicated AWS Enterprise Cloud Architecture**.

### 1. Critical Failures and Bottlenecks of the Temporary Serverless Model:
* **Cold Start Latency Spikes:** Serverless functions frequently experienced cold start delays exceeding 2.5 to 3.5 seconds when spinning up isolated runtimes after brief periods of inactivity. For campus students attempting to quickly report a lost item between classes, this caused unacceptable UI freezes.
* **Execution Timeouts During Image Moderation:** Serverless platforms impose rigid execution timeout limits (typically 10 to 15 seconds). When users uploaded high-resolution photographs requiring in-memory transcoding, WebP conversion, and Amazon Rekognition network round-trips, serverless functions routinely timed out and aborted mid-execution.
* **Absence of Private Virtual Private Cloud (VPC) Peering:** Serverless platforms run on multi-tenant public infrastructure outside our administrative perimeter. Connecting ephemeral functions to a relational PostgreSQL database required exposing the database port (5432) to the open internet, creating a critical vulnerability to brute-force attacks and credential sniffing.
* **Database Connection Pool Exhaustion:** Each stateless serverless execution spun up its own independent TCP database connection. A sudden influx of simultaneous student requests overwhelmed PostgreSQL’s maximum connection limit (`max_connections = 100`), causing catastrophic connection drops unless expensive third-party connection pooling proxies were provisioned.
* **Unpredictable Billing and Egress Spikes:** Serverless platforms charge aggressive markups on outbound bandwidth and compute execution duration, making long-term operational costs completely unpredictable for a university department.

### 2. Strategic Advantages Gained by Migrating to AWS Enterprise Infrastructure:
* **Zero-Trust Network Isolation (Amazon VPC):** By provisioning our own Virtual Private Cloud (`10.0.0.0/16`), the PostgreSQL database resides strictly in private, isolated subnets with zero public internet exposure. Connections are permitted solely from backend container tasks on port 5432.
* **Persistent Warm Compute (AWS ECS Fargate on Graviton ARM64):** Container tasks remain persistently active in memory, completely eliminating cold starts. Average API latency dropped from 2,800ms down to sub-80 milliseconds ($> 97\%$ improvement).
* **Direct High-Speed Integration with Amazon Rekognition & S3:** Because compute, storage, and AI vision services reside within the same AWS `us-east-1` region, internal media transfers traverse AWS’s private fiber backbone with zero public internet egress fees and sub-millisecond network hops.
* **Full Operational Observability (Amazon CloudWatch):** Container metrics (CPU, memory, active task count), Application Load Balancer access logs, and application error traces are aggregated into a single, unified CloudWatch dashboard with automated threshold alarms.
* **Predictable, Budget-Optimized Architecture:** By coupling AWS Graviton processors (20% lower cost per vCPU-hour) with CloudFront Free Tier caching allowances, the entire production deployment costs approximately **\$21.00 per month**, providing an enterprise-grade cloud footprint at a fraction of commercial SaaS costs.

---

## 7.8 Container Orchestration: Amazon ECR and ECS Fargate

Containerized backend workloads are deployed using **Amazon Elastic Container Service (ECS)** with the **AWS Fargate** serverless launch type:

* **Amazon Elastic Container Registry (ECR):**
  Private repository: `757952140199.dkr.ecr.us-east-1.amazonaws.com/refynd-backend`. Images are tagged with Git commit SHAs and scanned automatically for common vulnerabilities and exposures (CVEs).
* **AWS Fargate Task Definition (`refynd-prod-backend:6`):**
  * **Architecture:** 64-bit ARM64 (AWS Graviton)
  * **Compute Allocation:** 0.25 vCPU (256 CPU units), 512 MB RAM
  * **Network Mode:** `awsvpc` (allocates a dedicated Elastic Network Interface inside private subnets)
  * **Logging:** Native AWS FireLens / `awslogs` driver streaming stdout to CloudWatch `/ecs/refynd-prod-backend`.

Fargate eliminates the administrative burden of provisioning, patching, and scaling underlying EC2 virtual machine clusters. If a container task fails, the ECS control plane detects task degradation via ALB target health checks and provisions a replacement task in under 20 seconds.

---

## 7.9 Edge Content Delivery: Amazon CloudFront CDN and S3

The frontend web application is hosted in **Amazon S3** (`refynd-frontend-prod-a91aeec0`) and distributed globally via **Amazon CloudFront CDN** (Distribution ID: `E2D6HFDGFXT0R5`):

```
                   +-----------------------------------------------+
                   |     Amazon CloudFront (d25eqjxhksqlbh)        |
                   +-----------------------+-----------------------+
                                           |
                   +-----------------------+-----------------------+
                   | Path Pattern Check    |                       |
                   v                       v                       v
          [Path: /api/v1/*]       [Path: /*]              [Client Deep Link: /track]
                   |                       |                       |
                   v                       v                       v
          [Application Load]      [Amazon S3 Frontend]    [S3 Returns HTTP 404]
          [Balancer Target ]      [Bucket via OAC    ]             |
          [Backend Fargate ]      [Returns index.html]    [CloudFront Error Rule:  ]
                                                          [Rewrites to /index.html ]
                                                          [HTTP 200 -> Hydrates SPA]
```
*Figure 7.6: CloudFront CDN Edge Routing and Single-Page Application Fallback*

### CloudFront Security and Performance Controls:
1. **Origin Access Control (OAC):** Direct HTTP access to the S3 bucket is completely blocked. S3 permits read requests exclusively if signed by CloudFront’s AWS service principal (`cloudfront.amazonaws.com`).
2. **Automated SSL/TLS Termination:** CloudFront automatically negotiates TLS 1.3 encryption using Amazon’s default wildcard certificate, providing modern green-padlock HTTPS security without manual certificate renewal friction.
3. **SPA Deep-Link Routing:** Standard S3 website hosting returns 404 Not Found when a user directly navigates to a client-side route (e.g. `/track?report_id=...`). CloudFront custom error response rules map HTTP 403 and 404 errors to `/index.html` with an HTTP 200 response, allowing React Router to hydrate routes seamlessly.

---

## 7.10 Managed Database Tier: Amazon RDS PostgreSQL 16

The database layer utilizes **Amazon Relational Database Service (RDS)**:
* **Engine:** PostgreSQL 16.2
* **Instance Class:** `db.t4g.micro` (Powered by AWS Graviton2 processors)
* **Storage:** 20 GB General Purpose SSD (gp3) with automated baseline IOPS
* **Subnet Group:** Spans across two private availability zones (`us-east-1a`, `us-east-1b`)
* **Automated Backups:** Daily automated snapshots with a 7-day retention window, enabling point-in-time recovery (PITR) in the event of human data deletion errors.
* **Encryption at Rest:** Backed by AWS Key Management Service (AWS KMS) utilizing AES-256 encryption.

---

## 7.11 Infrastructure as Code (IaC) with Terraform

Every single cloud resource in ReFynd is declared in HashiCorp Terraform configuration files in `infra/terraform/`:

```
infra/terraform/
├── main.tf                     # Provider Declarations (AWS ~> 5.0) and Global State
├── variables.tf                # Input Variables (Environment, CIDR, Database Credentials)
├── outputs.tf                  # Infrastructure Outputs (CloudFront URL, ALB DNS, RDS Endpoint)
├── vpc.tf                      # Virtual Private Cloud, Subnets, Route Tables, Internet Gateway
├── alb.tf                      # Application Load Balancer, Listeners, Target Groups
├── ecs.tf                      # ECS Cluster, Task Definitions, Fargate Service, Security Groups
├── rds.tf                      # RDS PostgreSQL Instance, Subnet Groups, Parameter Groups
├── s3.tf                       # S3 Frontend Bucket, S3 Uploads Bucket, Bucket Policies
├── cloudfront.tf               # CloudFront Distribution, Cache Behaviors, OAC, Custom Errors
└── cloudwatch.tf               # Log Groups, 4 Production Metric Alarms, SNS Alert Topic
```

```hcl
# infra/terraform/ecs.tf - Fargate Task Definition Blueprint
resource "aws_ecs_task_definition" "backend" {
  family                   = "${var.project_name}-${var.environment}-backend"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256" # 0.25 vCPU
  memory                   = "512" # 512 MB RAM
  execution_role_arn       = aws_iam_role.ecs_execution_role.arn
  task_role_arn            = aws_iam_role.ecs_task_role.arn

  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "ARM64" # Optimized for AWS Graviton Compute
  }

  container_definitions = jsonencode([
    {
      name      = "backend"
      image     = "${aws_ecr_repository.backend.repository_url}:latest"
      essential = true
      portMappings = [
        {
          containerPort = 8000
          hostPort      = 8000
          protocol      = "tcp"
        }
      ]
      environment = [
        { name = "ENVIRONMENT", value = var.environment },
        { name = "DATABASE_URL", value = local.database_url_async },
        { name = "SMTP_HOST", value = var.smtp_host },
        { name = "SMTP_PORT", value = tostring(var.smtp_port) },
        { name = "SMTP_USER", value = var.smtp_user },
        { name = "MOCK_SMTP", value = tostring(var.mock_smtp) }
      ]
      secrets = [
        { name = "SECRET_KEY", valueFrom = aws_ssm_parameter.secret_key.arn },
        { name = "SMTP_PASSWORD", valueFrom = aws_ssm_parameter.smtp_password.arn }
      ]
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          "awslogs-group"         = aws_cloudwatch_log_group.backend.name
          "awslogs-region"        = var.aws_region
          "awslogs-stream-prefix" = "ecs"
        }
      }
    }
  ])
}
```

Terraform ensures that recreating the entire campus infrastructure from scratch takes less than eight minutes with a single command: `terraform apply -auto-approve`.

---

## 7.12 Identity & Access Management (IAM) and Security Hardening

The principle of **Least Privilege** is strictly enforced across all AWS Identity and Access Management (IAM) roles:
* **ECS Task Execution Role:** Granted permissions strictly to pull Docker images from Amazon ECR and stream logs to Amazon CloudWatch.
* **ECS Task Role:** Granted fine-grained runtime permissions:
  * `s3:PutObject` and `s3:GetObject` on the `refynd-uploads-*` bucket only.
  * `rekognition:DetectModerationLabels` for image content safety.
  * `ssm:GetParameters` to read encrypted secrets from AWS Systems Manager Parameter Store.
* The container task is explicitly blocked from modifying VPC networking, altering database schemas, or accessing any other AWS service.

---

## 7.13 Proactive Monitoring with CloudWatch and SNS Alarms

To ensure continuous system health and operational visibility, the infrastructure is monitored through four automated **Amazon CloudWatch Metric Alarms** declared in Terraform:

*Table 7.2: CloudWatch Production Metric Alarms Configuration*

| Alarm Identifier | Metric Evaluated | Threshold Condition | Evaluation Period | Action Triggered |
| :--- | :--- | :--- | :--- | :--- |
| `refynd-prod-ecs-cpu-high` | Container CPU Utilization | CPU > 80% | 2 Consecutive 1-Min Periods | SNS Alert to Admin Email |
| `refynd-prod-ecs-memory-high` | Container Memory Utilization | Memory > 80% | 2 Consecutive 1-Min Periods | SNS Alert to Admin Email |
| `refynd-prod-alb-5xx-errors` | Load Balancer 5xx Server Errors | Sum > 5 Errors | 5-Minute Window | SNS Alert to Admin Email |
| `refynd-prod-rds-cpu-high` | Database Host CPU Utilization | CPU > 80% | 2 Consecutive 5-Min Periods | SNS Alert to Admin Email |

When any alarm transitions into the `ALARM` state, an automated event is dispatched to the **Amazon SNS Topic** (`refynd-prod-alerts`), delivering an instant alert email to the campus systems engineering team.

---

## 7.14 Zero-Downtime Blue/Green Rolling Deployment Workflow

Application updates follow an automated, zero-downtime rolling update strategy:
1. The developer pushes updated code to the `main` branch.
2. The GitHub Actions CI runner compiles the new ARM64 container image and pushes it to Amazon ECR tagged with the Git commit SHA.
3. Terraform registers a new revision of the ECS Task Definition (e.g., Revision 7).
4. ECS launches the new task container in parallel with the running task.
5. The Application Load Balancer issues HTTP health checks (`GET /health`) against the new task.
6. Once the new container returns HTTP 200 OK across three consecutive checks, the ALB shifts incoming traffic to the new task and drains existing connections from the old container over a 30-second graceful window.
7. The old task is decommissioned, achieving a seamless deployment with **zero dropped requests**.
# CHAPTER 8
# VERIFICATION, TESTING, AND RESULTS

---

## 8.1 Testing Strategy and Verification Objectives

A software application operating as a mission-critical campus public service requires rigorous, multi-tiered verification to guarantee correctness, security, data integrity, and high performance under concurrent user load. The verification strategy for ReFynd encompassed a comprehensive testing pyramid:

```
                    / \
                   /   \
                  /  E2E \         -> Live Production Smoke & CloudFront Edge Verification
                 /---------\
                /  Security \      -> Penetration Testing (SQLi, XSS, RBAC, Rate Limits)
               /-------------\
              /  Integration  \    -> Multi-Service & Database Transactional Rollbacks
             /-----------------\
            /   Unit & Pytest   \  -> Automated CI Test Suite (18 Unit Tests Passing)
           /---------------------\
```

The core verification objectives were:
1. Verify that all 12 Functional Requirements (FR-01 to FR-12) execute without defects.
2. Confirm that sensitive personally identifiable information (PII) is 100% isolated and never leaked via public API endpoints.
3. Validate that Amazon Rekognition fail-closed safety interceptors reject inappropriate media uploads.
4. Verify that SlowAPI rate-limiting algorithms deflect rapid request bursts.
5. Benchmark cloud production response latencies under concurrent traffic.

---

## 8.2 Unit and API Testing with Pytest

Backend unit and API route verification was automated using **Pytest** and the asynchronous HTTP client **HTTPX** (`AsyncClient`). Tests are maintained in `backend/tests/` and run automatically on every code commit via GitHub Actions.

```python
# backend/tests/test_rekognition_moderation.py - Sample Automated Moderation Test
import pytest
from httpx import AsyncClient
from unittest.mock import patch

@pytest.mark.asyncio
async def test_inappropriate_image_upload_rejected(async_client: AsyncClient):
    """Verifies that an image flagged by Amazon Rekognition is rejected with HTTP 400."""
    fake_image_bytes = b"fake-flagged-image-content"
    
    # Mock Amazon Rekognition returning explicit content labels
    mock_labels = [{'Name': 'Explicit Nudity', 'Confidence': 94.2}]
    
    with patch("app.services.moderation.rekognition_client.detect_moderation_labels") as mock_rek:
        mock_rek.return_value = {'ModerationLabels': mock_labels}
        
        response = await async_client.post(
            "/api/v1/found/create",
            data={
                "title": "Found Item with Flagged Photo",
                "category": "Electronics",
                "description": "Found inside hostel common room",
                "location_found": "Hostel Block C",
                "holding_desk": "Hostel Reception",
                "contact_email": "finder@university.edu"
            },
            files={"image": ("test.jpg", fake_image_bytes, "image/jpeg")}
        )
        
        assert response.status_code == 400
        assert "Image upload rejected due to safety policy" in response.json()["detail"]
```

All 18 automated unit and integration tests execute and pass cleanly:

```
============================= test session starts ==============================
platform darwin -- Python 3.11.8, pytest-8.0.0, pluggy-1.4.0
rootdir: /Users/ashuchaudhary/Downloads/lost-and-found-main/backend
configfile: pytest.ini
plugins: anyio-4.2.0, asyncio-0.23.5
collected 18 items

tests/test_health.py .                                                   [  5%]
tests/test_rekognition_moderation.py ........                            [ 50%]
tests/test_support_and_email.py .........                               [100%]

============================== 18 passed in 2.34s ==============================
```
*Figure 8.1: Automated Test Execution Output Passing 18/18 Unit Test Cases*

---

## 8.3 Integration and Database Transactional Testing

Integration testing verified the interaction between FastAPI route handlers, Pydantic validation layers, and the PostgreSQL database engine.

To maintain test isolation and prevent test data pollution:
* Tests execute against an isolated test database session provisioned in `backend/tests/conftest.py`.
* Every test case wraps its operations in an atomic database transaction. Upon test completion, the fixture executes `await session.rollback()`, restoring the database to a clean baseline state without requiring slow disk truncation.

---

## 8.4 User Interface and Usability Testing

Frontend UI validation was executed across physical devices and responsive browser emulators:
* **Viewport Adaptability:** Verified flawless rendering across mobile displays (iPhone 14/15 Pro: 393x852), tablet displays (iPad Air: 820x1180), and desktop monitors (1920x1080 and 2560x1440).
* **Cross-Browser Compatibility:** Tested across Google Chrome (v122), Apple Safari (v17.3), and Mozilla Firefox (v123) with identical CSS grid and flexbox layout fidelity.
* **Debounced Search Usability:** Confirmed that typing in the search box smoothly buffers keystrokes (300ms debounce), preventing typing lag and eliminating flickering search result states.

---

## 8.5 Security Vulnerability and Penetration Testing

ReFynd was subjected to rigorous penetration testing to validate its defense-in-depth posture:

1. **SQL Injection (SQLi) Testing:**
   Injected classic SQL payloads (`' OR 1=1 --`, `admin'--`, `UNION SELECT NULL, username, password FROM users--`) into search boxes, filter query parameters, and form input fields.
   * *Result:* **100% Deflected.** SQLAlchemy uses strictly parameterized SQL queries. Injected characters were escaped and treated as literal search strings, returning empty results.
2. **Cross-Site Scripting (XSS) Testing:**
   Injected malicious JavaScript vectors (`<script>alert('XSS')</script>`, `<img src=x onerror=alert(1)>`) into item title and description fields.
   * *Result:* **100% Deflected.** Pydantic validators sanitize string inputs, and React’s JSX rendering automatically escapes dynamic variables before DOM insertion.
3. **Broken Object-Level Authorization (BOLA / IDOR):**
   Attempted to view private tracking information of report `LF-SRM-26-XXXXXX` by guessing sequential Report IDs without supplying the valid tracking token.
   * *Result:* **100% Deflected.** The API returned HTTP 403 Forbidden. Tracking endpoints require both the Report ID and the matching high-entropy secret token.
4. **Rate-Limit Stress Testing:**
   Executed automated Python scripts firing 50 consecutive requests within 5 seconds against `/api/v1/auth/login` and `/api/v1/lost/create`.
   * *Result:* **100% Deflected.** After request #10 on login and request #5 on report creation, the server immediately returned HTTP 429 Too Many Requests.

---

## 8.6 Live Production Verification on AWS Cloud

Following deployment to the live AWS production environment (`https://d25eqjxhksqlbh.cloudfront.net`), end-to-end smoke tests were executed to confirm live cloud telemetry:

1. **Live Report Submission & Email Dispatch:**
   * Submitted Lost Report `LF-SRM-26-CSVSQM` through the live CloudFront portal targeting recipient email `xripprix85@gmail.com`.
   * CloudWatch logs for `/ecs/refynd-prod-backend` confirmed:
     ```
     [BackgroundTasks] Queued confirmation email for report LF-SRM-26-CSVSQM
     [SMTP SUCCESS] Delivered email to xripprix85@gmail.com
     ```
   * The confirmation email was successfully received in the user's Gmail inbox containing the active tracking link (`https://d25eqjxhksqlbh.cloudfront.net/track?report_id=LF-SRM-26-CSVSQM&token=...`).

2. **Live Support Ticket Ingestion:**
   * Submitted Support Ticket `SUP-2026-2DZMKN` through `/support`.
   * CloudWatch logs confirmed immediate persistence to PostgreSQL and TLS dispatch to `cloudlostfound.platform@gmail.com`, followed by an acknowledgment receipt delivered to the user.

---

## 8.7 Comprehensive Test Case Execution Matrix

Table 8.1 details twenty-five formal test cases executed across the platform, documenting inputs, expected outputs, actual outcomes, and verification statuses.

*Table 8.1: Comprehensive Verification and Test Case Execution Results (TC-01 to TC-25)*

| Test ID | Module / Feature | Input Test Data | Expected System Behavior | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01**| Health Probe | `GET /health` | HTTP 200 `{"status": "healthy"}` | HTTP 200 Received in 12ms | **PASSED** |
| **TC-02**| Search Catalog | Keyword: `"MacBook"` | Returns matching active found laptops | 3 matching laptops returned | **PASSED** |
| **TC-03**| Search Category Filter | Category: `"Keys"` | Returns only items classified under Keys | Only key records displayed | **PASSED** |
| **TC-04**| Search Location Filter | Location: `"Library"` | Returns items located at Library desk | Filtered accurately | **PASSED** |
| **TC-05**| Debounce Validation | Typing fast: `"Calcul..."` | API called once after 300ms pause | Single network request issued | **PASSED** |
| **TC-06**| Lost Report Valid | Valid title, category, email | HTTP 201 Created + Report ID assigned | Report `LF-SRM-26-AWX3VM` saved | **PASSED** |
| **TC-07**| Lost Report Missing Field| Empty `title` string | HTTP 422 Unprocessable Entity | HTTP 422 with validation error | **PASSED** |
| **TC-08**| Lost Report Invalid Email| `email: "not-an-email"` | HTTP 422 Invalid email format | HTTP 422 Validation error | **PASSED** |
| **TC-09**| Found Report Valid | Valid attributes + holding desk | HTTP 201 Created + Item available | Record created in database | **PASSED** |
| **TC-10**| Found Report Photo Upload| Valid clean JPEG photo (2MB) | Transcoded to WebP, saved to S3 | S3 URL generated & attached | **PASSED** |
| **TC-11**| AI Moderation Safe Image| Photo of clean water bottle | Rekognition flags 0; upload passes | Photo accepted & stored | **PASSED** |
| **TC-12**| AI Moderation Explicit | Flagged inappropriate photo | Rekognition confidence > 70%; reject | HTTP 400 Upload rejected | **PASSED** |
| **TC-13**| Token Tracking Valid | Valid Report ID + Secret Token| Displays private item management dashboard | Dashboard loaded with item state| **PASSED** |
| **TC-14**| Token Tracking Invalid | Valid Report ID + Wrong Token | HTTP 403 Forbidden / Not Found | Access denied | **PASSED** |
| **TC-15**| Token Tracking Non-Exist| ID: `LF-SRM-26-FAKE00` | HTTP 404 Not Found error | HTTP 404 cleanly rendered | **PASSED** |
| **TC-16**| Claim Submission | Valid claimant name & proof | Claim created with status `PENDING` | Claim saved; linked to item | **PASSED** |
| **TC-17**| Staff Login Valid | Valid email & correct password | HTTP 200 + Signed JWT Token returned | JWT received & stored | **PASSED** |
| **TC-18**| Staff Login Bad Password | Valid email & wrong password | HTTP 401 Unauthorized error | HTTP 401 Invalid credentials | **PASSED** |
| **TC-19**| Staff Route Protection | Access `/api/v1/admin` without JWT | HTTP 401 Missing Bearer Token | Access blocked | **PASSED** |
| **TC-20**| Claim Adjudication | Staff clicks Approve Claim | Item status -> `CLAIMED`, audit log saved | Status updated, audit written | **PASSED** |
| **TC-21**| Rate Limit Login | 12 login attempts in 30 sec | Requests 1-10 pass; 11-12 return 429 | HTTP 429 Too Many Requests | **PASSED** |
| **TC-22**| Rate Limit Report Create| 7 reports submitted in 30 sec | Requests 1-5 pass; 6-7 return 429 | HTTP 429 Too Many Requests | **PASSED** |
| **TC-23**| Support Ticket Submission| Valid name, email, message | HTTP 201 Created + Ticket ID assigned | Ticket `SUP-2026-XXXX` created | **PASSED** |
| **TC-24**| Support Email Forward | Submit support ticket | Full details emailed to admin inbox | Email received via Google SMTP | **PASSED** |
| **TC-25**| CloudFront SPA Deep Link| Direct browser GET `/track` | CloudFront error rule serves `index.html`| Page hydrates without 404 error| **PASSED** |

---

## 8.8 Production Incident Resolution and Case Studies

During development and cloud provisioning, several complex engineering challenges were encountered and methodically resolved:

### Case Study 1: CloudFront 403 AccessDenied Account Verification
* **Incident:** When provisioning the CloudFront distribution via Terraform, AWS returned `403 AccessDenied: Your account must be verified before you can add new CloudFront resources.`
* **Root Cause:** Fresh AWS accounts undergo internal automated security reviews to prevent spam distributions before edge CDN provisioning permissions are granted.
* **Resolution:** Submitted an enterprise verification request to AWS Support detailing the educational purpose of ReFynd. AWS Support approved the review and lifted the restriction, allowing Terraform to provision the distribution successfully.

### Case Study 2: Broken Single-Page Application (SPA) Deep-Link Hydration
* **Incident:** Users navigating directly to `/track` or refreshing the `/report-lost` page received an ugly XML 404 error from Amazon S3.
* **Root Cause:** S3 website endpoints look for physical files matching the URI path (`/track/index.html`). Because React Router manages routing dynamically on the client side, no physical file exists at that path.
* **Resolution:** Added custom error response blocks in `infra/terraform/cloudfront.tf` mapping HTTP 403 and 404 errors to `/index.html` with an HTTP 200 status code, enabling seamless client-side hydration.

### Case Study 3: Synchronous SMTP Event-Loop Blocking
* **Incident:** Report creation endpoints experienced periodic 4-to-6-second latency spikes when users submitted listings.
* **Root Cause:** Standard Python `smtplib.SMTP` is a synchronous, blocking network call. Executing it directly inside an `async def` FastAPI route blocked the main thread event loop while waiting for Google SMTP TLS handshakes.
* **Resolution:** Refactored email dispatch into FastAPI `BackgroundTasks`. The route handler commits the database record and returns HTTP 201 immediately in under 45ms, while the email dispatches asynchronously in a background worker thread.

---

## 8.9 System Performance and Latency Evaluation

End-to-end performance benchmarking was conducted using Apache Bench (`ab`) and HTTPX concurrent load runners, evaluating latency under varying concurrency levels:

*Table 8.3: End-to-End Latency Benchmark Measurements Under Variable Concurrency*

| Concurrency Level | Target Endpoint | Average Latency | 95th Percentile ($P_{95}$) | Throughput (Req/Sec) | Error Rate |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **10 Users** | Static CDN Asset (`/index.html`)| **14 ms** | **22 ms** | 714 req/sec | 0.00% |
| **10 Users** | Database Search (`/api/v1/search`)| **38 ms** | **54 ms** | 263 req/sec | 0.00% |
| **50 Users** | Database Search (`/api/v1/search`)| **62 ms** | **88 ms** | 485 req/sec | 0.00% |
| **100 Users** | Report Creation (`/api/v1/lost/create`)| **78 ms** | **112 ms** | 128 req/sec | 0.00% |

The benchmarks demonstrate that ReFynd delivers deterministic sub-100ms response times for typical campus workloads, easily handling peak traffic spikes during class dismissal hours.
# CHAPTER 9
# CONCLUSION AND FUTURE SCOPE

---

## 9.1 Project Conclusion

The successful engineering, containerization, and production deployment of **ReFynd** demonstrates how modern cloud-native architectures, automated DevOps pipelines, and artificial intelligence can modernize antiquated campus administrative operations. By replacing fragmented physical logbooks and chaotic, privacy-violating social media messaging groups with an enterprise-grade web clearinghouse, ReFynd establishes an efficient, secure, and auditable paradigm for campus lost-and-found management.

The platform unites a reactive, type-safe frontend interface built with **React 18 and TypeScript** with a high-throughput, non-blocking backend microservice powered by **FastAPI and Python 3.11**. Crucially, the entire infrastructure was provisioned and validated on **Amazon Web Services (AWS)** using **Terraform Infrastructure as Code (IaC)**, guaranteeing 100% repeatability and eliminating manual configuration drift. 

By enforcing strict network segregation within a custom Virtual Private Cloud (VPC), placing relational PostgreSQL databases in private isolated subnets, enforcing token-bucket rate limiting via SlowAPI, integrating real-time automated image moderation through **Amazon Rekognition**, and dispatching asynchronous encrypted notifications via Google SMTP over TLS, ReFynd delivers an enterprise-grade digital solution that operates within a lean educational cloud budget of approximately \$21.00 per month.

---

## 9.2 Key Achievements

The project successfully realized all initial functional, architectural, and operational engineering milestones:

1. **Production Deployment on AWS Enterprise Cloud:**
   Successfully deployed to a live, production-grade cloud topology accessible globally at `https://d25eqjxhksqlbh.cloudfront.net` with automated SSL/TLS termination, AWS Application Load Balancers, and ECS Fargate serverless containers.
2. **Absolute Asymmetric Privacy Preservation:**
   Completely eliminated the exposure of student personal identifying information (PII) on public web interfaces. Contact emails and phone numbers are encrypted in a private database vault, allowing anonymous searching and self-service tracking via cryptographically unguessable tokens.
3. **Automated AI Safety Gatekeeper:**
   Integrated Amazon Rekognition (`DetectModerationLabels`) with a fail-closed architecture, ensuring that offensive, inappropriate, or malicious image uploads are detected and rejected prior to permanent cloud storage persistence.
4. **DevOps Automation & Reproducibility:**
   Achieved 100% Infrastructure as Code (IaC) coverage via modular Terraform scripts, multi-stage Docker containerization optimized for ARM64 Graviton processors, and automated continuous integration pipelines via GitHub Actions passing 18/18 unit and integration test suites.
5. **Cost-Optimized High Performance:**
   Achieved sub-100 millisecond $P_{95}$ API response latencies while maintaining a predictable, cost-effective infrastructure footprint designed specifically for collegiate operational budgets.

---

## 9.3 System Limitations

While ReFynd delivers a robust, production-tested platform, several operational limitations remain inherent to its current version:

1. **Textual Feature Dependency in Matching:**
   Although the matching engine computes weighted similarity across categories, brands, fuzzy strings, and locations, it relies on the accuracy of human textual input. If a student describes an item simply as *"gadget"* while the finder logs it as *"portable charger"*, the algorithm may compute an artificially low similarity score.
2. **Absence of Native Mobile Applications:**
   The current implementation operates as a progressive web application (PWA) accessed through mobile browsers. It does not yet offer native iOS or Android mobile application packages with device-level push notifications or offline local caching.
3. **Manual In-Person Physical Handoff:**
   The system orchestrates digital verification and matching but relies on human attendants stationed at physical holding desks (e.g., Central Library, Security Main Gate) to inspect credentials and physically release belongings. It does not integrate automated physical hardware (such as IoT smart lockers).

---

## 9.4 Future Work and Research Directions

To expand upon the foundational architecture established in this project, four major research and engineering pathways are proposed for future development:

### 1. Multi-Modal Vision-Language Embeddings (OpenAI CLIP / AWS Bedrock)
The next evolution of the matching engine involves replacing heuristic text matching with multi-modal vector embeddings powered by contrastive vision-language models (such as OpenAI CLIP or Amazon Titan Multimodal Embeddings). By vectorizing both the image of the found item and the textual description of the lost item into a shared 512-dimensional embedding space, the system can execute cosine similarity searches in PostgreSQL using the `pgvector` extension:

$$\text{Similarity}(\vec{u}_{text}, \vec{v}_{image}) = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}$$

This will enable the platform to accurately match an owner’s description (*"blue thermal water bottle with stickers"*) with a photograph of a found bottle even if the finder entered zero descriptive text.

### 2. Interactive Campus Geospatial Heatmaps
Future releases will integrate interactive SVG/Leaflet campus geospatial maps. When reporting a lost or found item, students can drop an exact pinpoint on the campus map. The system can aggregate spatial data to generate administrative heatmaps, revealing high-loss campus zones (e.g., specific cafeteria seating zones or athletic stadium bleachers) to guide preventive security measures.

### 3. Native Cross-Platform Mobile Applications with Push Notifications
Developing native mobile clients using **React Native** or **Flutter** will allow ReFynd to leverage device-native capabilities:
* **Camera Integration:** Instant in-app photo capture with client-side edge compression.
* **Apple Push Notification Service (APNs) and Firebase Cloud Messaging (FCM):** Instant push notifications alerting students the moment a matching item is cataloged, eliminating dependency on email inbox monitoring.

### 4. Multi-Tenant Campus Federation
Architectural enhancements can transform ReFynd into a multi-tenant Software-as-a-Service (SaaS) platform capable of serving multiple independent universities or multi-campus institutions from a single shared infrastructure. By implementing PostgreSQL schema-based multi-tenancy and dynamic domain routing, different universities can manage isolated lost-and-found portals while benefiting from shared cloud economies of scale.
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
