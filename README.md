 <div align="center">

# ◈ OPSPILOT AI

### THE EVIDENCE-FIRST OPERATIONS INTELLIGENCE PLATFORM

**Observe. Correlate. Investigate. Understand.**

Turning operational events into structured, traceable incident investigations.

[EXPLORE REPOSITORY](https://github.com/akankshad1712/opspilot-ai) · [DEVELOPER PROFILE](https://github.com/akankshad1712) · [LINKEDIN](https://linkedin.com/in/akanksha-deshmukh-26210b244) · [PORTFOLIO](https://akankshadeshmukh.com)

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-5.7-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-8B5CF6?style=for-the-badge)

</div>

---

<div align="center">

### ENGINEERING VISIBILITY FOR OPERATIONAL COMPLEXITY

| EVENT INTELLIGENCE | INCIDENT CONTEXT | EVIDENCE CORRELATION | AUDITABILITY |
|:---:|:---:|:---:|:---:|
| Collect | Organize | Investigate | Trace |

</div>

## 00 — THE PRODUCT

Operational incidents rarely arrive with a complete explanation.

An application may generate hundreds of events across services and environments. Engineers must determine which signals matter, what happened around the incident, and which explanations are supported by available evidence.

**OpsPilot AI** provides a structured incident investigation workflow that brings these activities into one application.

It combines a Python backend, a deterministic investigation engine, persistent data models, audit logging, and a React dashboard.

### The core proposition

> Don't jump from an alert to a conclusion. Build the explanation from evidence.

### What the application implements

| System capability | Implementation |
|---|---|
| Operational event ingestion | REST API |
| Incident creation and retrieval | Incident management endpoints |
| Related-event retrieval | Service, environment, and time filtering |
| Error signal classification | Severity-based rules |
| Deployment signal classification | Source-based rules |
| Investigation generation | Deterministic Python engine |
| Confidence calculation | Bounded heuristic scoring |
| Investigation persistence | SQLAlchemy models |
| Repeated investigation handling | Updates existing investigation |
| Audit history | Persistent audit records |
| Incident dashboard | React and TypeScript |
| Background processing | Separate polling worker |

---

## 01 — VISUAL SYSTEM BLUEPRINT

### The application at a glance

```mermaid
flowchart TB
    subgraph L1["01 · OPERATIONAL INPUT"]
        A["Operational Events"]
        B["Incident Context"]
    end

    subgraph L2["02 · APPLICATION CONTROL"]
        C["FastAPI REST Layer"]
        D["Event Services"]
        E["Incident Services"]
    end

    subgraph L3["03 · INVESTIGATION INTELLIGENCE"]
        F["Evidence Retrieval"]
        G["Signal Classification"]
        H["Deterministic Investigation"]
    end

    subgraph L4["04 · PERSISTENCE"]
        I[("SQLAlchemy / Database")]
        J["Audit History"]
    end

    subgraph L5["05 · PRESENTATION"]
        K["React Dashboard"]
        M["Investigation Findings"]
    end

    A --> C
    B --> C
    C --> D
    C --> E
    D --> I
    E --> I
    D --> F
    E --> F
    F --> G
    G --> H
    H --> I
    H --> J
    I --> K
    J --> K
    K --> M

    classDef input fill:#14264A,stroke:#60A5FA,color:#FFFFFF
    classDef control fill:#12374A,stroke:#22D3EE,color:#FFFFFF
    classDef intelligence fill:#292044,stroke:#A78BFA,color:#FFFFFF
    classDef storage fill:#103C32,stroke:#34D399,color:#FFFFFF
    classDef presentation fill:#3B2750,stroke:#C084FC,color:#FFFFFF

    class A,B input
    class C,D,E control
    class F,G,H intelligence
    class I,J storage
    class K,M presentation
```

*Conceptual architecture of the implemented application. The layered presentation is a documentation view, not a claim that every layer is a separate deployed service.*

### Architecture responsibility matrix

| Layer | Primary responsibility | Technology |
|---|---|---|
| Presentation | User interaction and investigation display | React, TypeScript |
| API | HTTP request handling | FastAPI |
| Business logic | Event and incident operations | Python |
| Investigation | Evidence selection and signal scoring | Python |
| Persistence | Models and database sessions | SQLAlchemy |
| Storage | Local persistent data | SQLite by default |
| Background execution | Periodic investigation of open incidents | Python worker |

---

## 02 — EVENT-TO-INVESTIGATION LIFECYCLE

### How information moves through the application

```mermaid
flowchart TD
    A(["START · Operational Activity"]) --> B["Receive Structured Event"]
    B --> C["Validate Request"]
    C --> D["Persist Event"]
    D --> E["Record EVENT_INGESTED"]

    F(["Incident Created"]) --> G["Persist Incident"]
    G --> H["Record INCIDENT_CREATED"]

    E --> I["Incident Investigation Request"]
    H --> I

    I --> J["Load Incident Context"]
    J --> K["Retrieve Candidate Events"]
    K --> L["Apply Context Filters"]

    L --> M["Detect Error Signals"]
    L --> N["Detect Deployment Signals"]

    M --> O["Calculate Investigation Score"]
    N --> O

    O --> P["Generate Hypothesis"]
    P --> Q["Generate Recommendation"]
    Q --> R["Persist Investigation"]
    R --> S["Record INVESTIGATION_GENERATED"]
    S --> T(["RETURN · Investigation Result"])

    classDef start fill:#123D35,stroke:#34D399,color:#FFFFFF
    classDef processing fill:#142C49,stroke:#38BDF8,color:#FFFFFF
    classDef intelligence fill:#2C2148,stroke:#A78BFA,color:#FFFFFF
    classDef finish fill:#3B2750,stroke:#C084FC,color:#FFFFFF

    class A,F,T start
    class B,C,D,E,G,H,I,J,K,L processing
    class M,N,O,P,Q intelligence
    class R,S finish
```

### Investigation sequence

```mermaid
sequenceDiagram
    autonumber
    actor User as Engineer
    participant Web as React Dashboard
    participant API as FastAPI
    participant Engine as Investigation Engine
    participant DB as SQLAlchemy Database

    User->>Web: Select an incident
    Web->>API: GET incident details
    API->>DB: Load incident and related events
    DB-->>API: Return records
    API-->>Web: Incident information

    User->>Web: Run investigation
    Web->>API: POST /investigate
    API->>Engine: Execute investigation
    Engine->>DB: Retrieve matching events
    DB-->>Engine: Return evidence
    Engine->>Engine: Classify signals
    Engine->>Engine: Calculate score and findings
    Engine->>DB: Persist investigation
    Engine->>DB: Write audit record
    API-->>Web: Investigation response
    Web-->>User: Display findings
```

---

## 03 — THE INVESTIGATION ENGINE

### Evidence selection strategy

The engine selects related events using the incident's service, environment, and start time.

| Dimension | Current selection rule |
|---|---|
| Service | Event service matches incident service |
| Environment | Event environment matches incident environment |
| Start boundary | 30 minutes before incident start |
| End boundary | 2 hours after incident start |
| Event ordering | Timestamp ascending |

This creates a bounded evidence set before signal evaluation.

### Signal classification

| Signal family | Detection condition | Interpretation |
|---|---|---|
| Error | Severity is `ERROR` | Error event |
| Critical | Severity is `CRITICAL` | Critical event |
| Deployment | Source is `deployment` | Deployment-related event |
| Deploy | Source is `deploy` | Deployment-related event |
| Release | Source is `release` | Release-related event |

### Confidence scoring model

The current engine uses an explicit deterministic scoring heuristic.

| Component | Rule | Maximum contribution |
|---|---|---:|
| Baseline | Initial score | 0.25 |
| Error evidence | 0.05 per error/critical event | 0.30 |
| Deployment correlation | Added when errors and deployment signals both exist | 0.25 |
| Final cap | Maximum permitted score | 0.95 |

```python
score = 0.25

score += min(error_count * 0.05, 0.30)

if has_deployment and has_errors:
    score += 0.25

score = min(score, 0.95)

confidence = round(score, 2)
```

### Decision flow

```mermaid
flowchart TD
    A["Start"] --> B["Load Related Evidence"]
    B --> C["Count ERROR / CRITICAL Signals"]
    B --> D["Identify Deployment Signals"]

    C --> E["Start at 0.25"]
    D --> E

    E --> F["Add Capped Error Contribution"]
    F --> G{"Errors and Deployment Present?"}

    G -->|Yes| H["Add 0.25"]
    G -->|No| I["Keep Current Score"]

    H --> J["Cap Score at 0.95"]
    I --> J

    J --> K["Round to Two Decimal Places"]
    K --> L["Generate Hypothesis"]
    L --> M["Generate Recommendation"]
    M --> N["Persist Result"]
```

### Finding interpretation

The engine generates findings based on the observed signals.

| Evidence situation | Current interpretation |
|---|---|
| No qualifying error signals | Insufficient evidence |
| Error signals found | Error-signal hypothesis |
| Deployment and errors found | Possible temporal deployment correlation |
| Repeated investigation | Update existing investigation record |

**Important engineering boundary:** the confidence score is not a calibrated probability. A temporal deployment correlation does not prove causation. Recommendations do not execute remediation.

---

## 04 — DATA ARCHITECTURE

### Persistence model

```mermaid
erDiagram
    INCIDENT ||--o| INVESTIGATION : has
    INCIDENT ||--o{ AUDIT_LOG : records

    INCIDENT {
        int id PK
        string title
        string service
        string environment
        datetime started_at
        string status
    }

    EVENT {
        int id PK
        string source
        string service
        string environment
        datetime timestamp
        string severity
        string message
        json metadata
    }

    INVESTIGATION {
        int id PK
        int incident_id FK
        string summary
        float confidence
        int evidence_count
        string hypothesis
        string recommendation
    }

    AUDIT_LOG {
        int id PK
        int incident_id FK
        string action
        string actor
        json detail
        datetime created_at
    }
```

### Entity responsibility

| Model | Responsibility |
|---|---|
| `Event` | Stores structured operational events |
| `Incident` | Stores incident context and status |
| `Investigation` | Stores generated findings and confidence |
| `AuditLog` | Records application activities |

Events are retrieved through matching attributes and time criteria. The diagram intentionally does not imply a direct event-to-incident foreign-key relationship.

### Audit activity

The application records the following actions:

| Action | Trigger |
|---|---|
| `EVENT_INGESTED` | Event ingestion |
| `INCIDENT_CREATED` | Incident creation |
| `INVESTIGATION_GENERATED` | Investigation execution |

Audit records include an action, actor, detail payload, and timestamp.

---

## 05 — REST API REFERENCE

**Local API base URL**

```text
http://127.0.0.1:8000
```

### Health

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | API health check |

### Events

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/v1/events` | Ingest event |
| GET | `/api/v1/events` | Retrieve events |

### Incidents

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/v1/incidents` | Create incident |
| GET | `/api/v1/incidents` | List incidents |
| GET | `/api/v1/incidents/{incident_id}` | Retrieve incident details |

### Investigation

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/v1/incidents/{incident_id}/investigate` | Generate investigation |

### Audit

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/v1/incidents/{incident_id}/audit` | Retrieve audit history |

### Interactive API exploration

After starting the backend, open:

**Swagger UI:** `http://127.0.0.1:8000/docs`

---

## 06 — FRONTEND EXPERIENCE

The current React application provides an incident-focused investigation dashboard.

| Interface area | Implemented behavior |
|---|---|
| Incident list | Browse available incidents |
| Incident details | Inspect selected incident |
| Evidence timeline | Review related events |
| Investigation action | Trigger an investigation |
| Confidence display | Review heuristic score |
| Summary | Read generated investigation summary |
| Hypothesis | Review possible explanation |
| Recommendation | View suggested next step |

### User interaction flow

```mermaid
flowchart LR
    A["Open Dashboard"] --> B["Select Incident"]
    B --> C["Review Incident Context"]
    C --> D["Inspect Evidence"]
    D --> E["Run Investigation"]
    E --> F["Review Confidence"]
    F --> G["Read Hypothesis"]
    G --> H["Review Recommendation"]
```

The current frontend API base URL is `http://localhost:8000`.

---

## 07 — OPTIONAL BACKGROUND WORKER

The repository contains a separate Python worker process.

### Current worker behavior

```mermaid
flowchart TD
    A["Worker Starts"] --> B["Open Database Session"]
    B --> C["Find Up To 10 OPEN Incidents"]
    C --> D{"Any Open Incidents?"}
    D -->|Yes| E["Investigate Each Incident"]
    D -->|No| F["Wait"]
    E --> G["Close Database Session"]
    G --> F
    F --> H["Sleep WORKER_INTERVAL"]
    H --> B
```

| Property | Current behavior |
|---|---|
| Process | `apps/worker/main.py` |
| Incident filter | OPEN incidents |
| Batch size | Up to 10 |
| Default polling interval | 30 seconds |
| Execution | Separate process |

This is a polling-based prototype worker, not a distributed message queue or production scheduling system.

---

## 08 — TECHNOLOGY STACK

| Category | Technology | Role |
|---|---|---|
| Backend | Python 3.12 | Application logic |
| API | FastAPI 0.115 | REST endpoints |
| Validation | Pydantic | Data validation |
| Persistence | SQLAlchemy 2.0 | ORM |
| Database | SQLite | Default local database |
| Database connectivity | psycopg | PostgreSQL driver dependency |
| Frontend | React 19 | UI |
| Frontend language | TypeScript 5.7 | Typed frontend |
| Build tooling | Vite 6 | Frontend tooling |
| Server | Uvicorn | ASGI server |
| Testing | Pytest | Backend tests |
| API test client | HTTPX | HTTP-level testing |
| Coverage | Coverage.py | Backend coverage |
| Containers | Docker | Container packaging |
| Local orchestration | Docker Compose | API and web startup |
| Version control | Git | Source control |

---

## 09 — REPOSITORY MAP

```text
opspilot-ai/
│
├── apps/
│   │
│   ├── api/
│   │   └── app/
│   │       ├── __init__.py
│   │       ├── config.py
│   │       ├── database.py
│   │       ├── engine.py
│   │       ├── main.py
│   │       ├── models.py
│   │       ├── schemas.py
│   │       └── services.py
│   │
│   ├── web/
│   │   ├── src/
│   │   │   ├── App.tsx
│   │   │   ├── main.tsx
│   │   │   └── styles.css
│   │   ├── index.html
│   │   ├── package.json
│   │   └── vite.config.ts
│   │
│   └── worker/
│       └── main.py
│
├── tests/
│   └── test_api.py
│
├── docs/
├── data/
│
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 10 — LOCAL DEVELOPMENT

### Prerequisites

| Dependency | Version |
|---|---|
| Python | 3.12 |
| Node.js | 22 recommended |
| npm | Included with Node.js |
| Git | Recent version |
| Docker | Optional |

### Windows PowerShell installation

**01 — Clone the repository**

```powershell
git clone https://github.com/akankshad1712/opspilot-ai.git

cd opspilot-ai
```

**02 — Create virtual environment**

```powershell
python -m venv .venv

.\.venv\Scripts\Activate.ps1
```

**03 — Install backend dependencies**

```powershell
python -m pip install -r requirements.txt
```

**04 — Create local environment configuration**

```powershell
Copy-Item .env.example .env
```

Default configuration:

```env
DATABASE_URL=sqlite:///./opspilot.db
API_HOST=0.0.0.0
API_PORT=8000
CORS_ORIGINS=http://localhost:5173
```

**05 — Start backend**

```powershell
python -m uvicorn apps.api.app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

**06 — Start frontend**

Open a second PowerShell terminal:

```powershell
cd C:\Users\hp\Desktop\opspilot-ai\apps\web

npm install

npm run dev
```

Frontend:

```text
http://localhost:5173
```

**07 — Verify services**

| Service | Address |
|---|---|
| Web application | `http://localhost:5173` |
| Backend API | `http://127.0.0.1:8000` |
| API documentation | `http://127.0.0.1:8000/docs` |
| Health endpoint | `http://127.0.0.1:8000/health` |

---

## 11 — DOCKER EXECUTION

The repository includes Docker and Docker Compose configuration for local API and frontend services.

Create the environment file:

```powershell
Copy-Item .env.example .env
```

Build and start:

```powershell
docker compose up --build
```

Stop:

```powershell
docker compose down
```

The optional worker is run separately; it is not part of the current Compose service set.

---

## 12 — TESTING & ENGINEERING VERIFICATION

### Run the backend suite

```powershell
python -m pytest -v
```

### Generate backend coverage

Install Coverage.py:

```powershell
python -m pip install coverage
```

Run branch-aware coverage:

```powershell
python -m coverage run --branch --source=apps.api.app -m pytest -v

python -m coverage report -m
```

### Verified results

| Quality indicator | Result |
|---|---:|
| Backend tests passed | 15 |
| Backend statement coverage | 100% |
| Backend branch coverage | 100% |
| Coverage target | `apps.api.app` |

### Verified coverage by module

| Module | Statement coverage |
|---|---:|
| `config.py` | 100% |
| `database.py` | 100% |
| `engine.py` | 100% |
| `main.py` | 100% |
| `models.py` | 100% |
| `schemas.py` | 100% |
| `services.py` | 100% |
| **Backend total** | **100%** |

### Test coverage areas

- Health endpoint.
- Event ingestion and retrieval.
- Incident creation and retrieval.
- Missing incident handling.
- Related-event filtering.
- Investigation generation.
- Repeated investigation updates.
- Audit history.
- Database session cleanup.

**Coverage qualification:** this is verified backend application-package coverage. It is not a statement about frontend coverage, end-to-end coverage, load testing, or production reliability.

---

## 13 — ENGINEERING DECISIONS

| Decision | Reason |
|---|---|
| REST API architecture | Clear boundary between client and backend |
| FastAPI | Structured API development and validation |
| SQLAlchemy ORM | Explicit database models and relationships |
| SQLite default | Simple local development |
| Deterministic investigation | Reproducible and inspectable behavior |
| Bounded time window | Controls evidence relevance |
| Separate investigation model | Separates incident context from generated findings |
| Audit logging | Records important operational actions |
| Optional polling worker | Demonstrates background execution |
| Pytest and HTTPX | Verifies backend behavior |

---

## 14 — IMPLEMENTATION STATUS

A clear distinction between current capabilities and future work is part of the project's engineering documentation.

| Feature | Status |
|---|---|
| FastAPI application | Implemented |
| Event ingestion API | Implemented |
| Event retrieval API | Implemented |
| Incident creation API | Implemented |
| Incident retrieval API | Implemented |
| Related event retrieval | Implemented |
| Deterministic investigation | Implemented |
| Confidence heuristic | Implemented |
| Hypothesis generation | Implemented |
| Recommendation generation | Implemented |
| Investigation persistence | Implemented |
| Audit logging | Implemented |
| React incident dashboard | Implemented |
| Separate polling worker | Implemented |
| Docker configuration | Implemented |
| Backend automated tests | Implemented |
| Production LLM integration | Not implemented |
| Kafka streaming | Not implemented |
| Redis caching | Not implemented |
| Authentication and RBAC | Not implemented |
| Autonomous remediation | Not implemented |
| Human approval workflow | Not implemented |
| Frontend automated test suite | Not implemented |

---

## 15 — ENGINEERING ROADMAP

```mermaid
flowchart TD
    A["CURRENT FOUNDATION"] --> B["ADVANCED EVENT PROCESSING"]
    B --> C["EXPANDED CORRELATION"]
    C --> D["AI-ASSISTED INVESTIGATION"]
    D --> E["SECURE ACCESS & GOVERNANCE"]
    E --> F["CONTROLLED REMEDIATION"]

    A --- A1["Current FastAPI + React MVP"]
    B --- B1["Potential Kafka integration"]
    C --- C1["Richer evidence relationships"]
    D --- D1["Evidence-linked model assistance"]
    E --- E1["Authentication and approvals"]
    F --- F1["Policy-controlled actions"]

    classDef current fill:#123D35,stroke:#34D399,color:#FFFFFF
    classDef future fill:#172A49,stroke:#60A5FA,color:#FFFFFF

    class A,A1 current
    class B,B1,C,C1,D,D1,E,E1,F,F1 future
```

Potential next engineering milestones:

1. Validate PostgreSQL deployment and migrations.
2. Add richer event correlation.
3. Introduce integration and end-to-end testing.
4. Add frontend automated tests.
5. Implement authentication and role-based access.
6. Evaluate evidence-linked AI assistance.
7. Design human approval and policy controls.
8. Investigate safe, controlled remediation workflows.

These are roadmap items, not claims about the current application.

---

## 16 — SECURITY & OPERATIONAL CONSIDERATIONS

The current project is an MVP and should not be treated as a production incident-management deployment.

Before production use, the following areas require additional implementation and validation:

| Area | Additional work |
|---|---|
| Authentication | Identity and session management |
| Authorization | Role-based access control |
| Secrets | Secure secret storage |
| Database | Production database configuration and migrations |
| API protection | Rate limiting and abuse controls |
| Observability | Structured application logging and metrics |
| Reliability | Deployment, recovery, and backup procedures |
| Testing | Integration, security, and load testing |
| Remediation | Explicit policy and human approval controls |

Never commit real credentials, tokens, private keys, or production environment files.

---

## 17 — DOCUMENTATION & RESOURCES

| Resource | Link |
|---|---|
| Source repository | [GitHub](https://github.com/akankshad1712/opspilot-ai) |
| API documentation | `/docs` after starting the backend |
| Security policy | [SECURITY.md](SECURITY.md) |
| License | [LICENSE](LICENSE) |

---

## 18 — ABOUT THE DEVELOPER

<div align="center">

# AKANKSHA DESHMUKH

### SOFTWARE DEVELOPER

Interested in backend engineering, full-stack development, API design, application architecture, and practical software engineering.

[![GitHub](https://img.shields.io/badge/GitHub-akankshad1712-181717?style=for-the-badge&logo=github)](https://github.com/akankshad1712)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/akanksha-deshmukh-26210b244)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-8B5CF6?style=for-the-badge)](https://akankshadeshmukh.com)
[![LeetCode](https://img.shields.io/badge/LeetCode-Kanksha17-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/Kanksha17/)

</div>

---

<div align="center">

### ◈ OPSPILOT AI

**SEE THE SIGNAL. UNDERSTAND THE INCIDENT. FOLLOW THE EVIDENCE.**

Designed around clarity. Built around evidence. Documented with engineering transparency.

</div>
