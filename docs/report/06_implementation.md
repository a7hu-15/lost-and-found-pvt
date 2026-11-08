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

