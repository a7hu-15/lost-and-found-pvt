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
