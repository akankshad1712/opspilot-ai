<!--
  OPSPILOT AI
  Premium GitHub Project README
  Visual identity: Midnight / Electric Violet / Cyan
-->

<div align="center">

# ◈ OPSPILOT AI

### THE INTELLIGENCE LAYER FOR OPERATIONAL CLARITY.

**From scattered system events to evidence-backed incident intelligence.**

A modern operations intelligence platform for ingesting events, managing incidents, investigating operational signals, and transforming technical evidence into actionable insights.

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=111111)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-Frontend-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

<br/>

[**Explore Repository**](https://github.com/akankshad1712/opspilot-ai)
&nbsp; ◆ &nbsp;
[**Author Profile**](https://github.com/akankshad1712)
&nbsp; ◆ &nbsp;
[**Connect on LinkedIn**](https://linkedin.com/in/akanksha-deshmukh-26210b244)

<br/>

</div>

---

<div align="center">

## ◈ THE BIG IDEA

### Operations should be understandable, not overwhelming.

</div>

Modern software systems generate continuous streams of events, errors, deployments, and operational signals.

The challenge isn't simply collecting those signals. It's understanding which signals matter, how they relate to an incident, and what the evidence actually tells us.

**OpsPilot AI** addresses this challenge through an evidence-first investigation workflow.

Instead of presenting disconnected operational information, the platform connects relevant events to incidents, evaluates investigation signals, calculates confidence, and records the investigation history.

> **Core philosophy:** Every investigation should have evidence. Every recommendation should have context. Every important action should be traceable.

---

# 01 — PRODUCT EXPERIENCE

<div align="center">

### ONE PLATFORM. FOUR OPERATIONAL CAPABILITIES.

</div>

<table>
<tr>
<td width="50%" valign="top">

### ◉ Event Intelligence

Collect and organize operational events through REST APIs.

- Event ingestion
- Structured event metadata
- Service and environment context
- Event retrieval

</td>
<td width="50%" valign="top">

### ◈ Incident Management

Create and manage incidents through a centralized workflow.

- Incident creation
- Incident retrieval
- Incident details
- Related event association

</td>
</tr>
<tr>
<td width="50%" valign="top">

### ⌁ Evidence-Based Investigation

Analyze operational signals using a deterministic investigation engine.

- Related event filtering
- Error and deployment signals
- Confidence scoring
- Investigation recommendations

</td>
<td width="50%" valign="top">

### ◷ Audit Intelligence

Preserve investigation history and operational traceability.

- Incident activity records
- Investigation history
- Audit retrieval
- Structured audit details

</td>
</tr>
</table>

---

# 02 — HOW THE SYSTEM THINKS

<div align="center">

### THE OPSPILOT INVESTIGATION PIPELINE

*From an incoming event to an evidence-backed investigation.*

</div>

```mermaid
flowchart TD
    A(["Incoming Operational Events"]) --> B["Event Ingestion API"]
    B --> C[("Structured Event Storage")]

    D(["Incident Created"]) --> E["Incident Management API"]

    C --> F["Evidence Retrieval"]
    E --> F

    F --> G{"Relevant Evidence Found?"}

    G -->|"Yes"| H["Service & Environment Matching"]
    H --> I["Time-Window Filtering"]
    I --> J["Error & Deployment Signal Analysis"]

    G -->|"No"| K["Limited Evidence Assessment"]

    J --> L["Confidence Score Calculation"]
    K --> L

    L --> M["Investigation Findings"]
    M --> N["Recommendations"]
    N --> O[("Investigation Audit History")]

    O --> P(["Operational Insights"])

    classDef input fill:#171A2D,stroke:#8B5CF6,color:#FFFFFF
    classDef process fill:#10283A,stroke:#22D3EE,color:#FFFFFF
    classDef decision fill:#332451,stroke:#A78BFA,color:#FFFFFF
    classDef storage fill:#102E2A,stroke:#34D399,color:#FFFFFF
    classDef output fill:#20213C,stroke:#818CF8,color:#FFFFFF

    class A,D input
    class B,E,F,H,I,J,L,M,N process
    class G decision
    class C,O storage
    class P output
```

### Investigation logic

The current investigation engine uses deterministic rules rather than claiming to rely on a production LLM.

Its workflow includes:

1. Identifying events associated with the incident's service and environment.
2. Filtering relevant events within a defined time window.
3. Evaluating error and deployment signals.
4. Calculating a confidence score from the available evidence.
5. Producing findings and recommendations.
6. Recording investigation activity.

**Current scoring model:** The engine starts with a baseline score, increases it based on relevant error signals and deployment-plus-error combinations, and caps the result at 0.95.

This makes the current investigation workflow understandable, reproducible, and testable.

---

# 03 — SYSTEM ARCHITECTURE

<div align="center">

### MODULAR BY DESIGN. EVIDENCE-DRIVEN BY DEFAULT.

</div>

```mermaid
flowchart TB

    subgraph CLIENT["01  —  PRESENTATION LAYER"]
        UI["React 19"]
        TS["TypeScript"]
        VITE["Vite"]
        UI --- TS
        TS --- VITE
    end

    subgraph API["02  —  APPLICATION LAYER"]
        FAST["FastAPI"]
        EVENT["Event Management"]
        INCIDENT["Incident Management"]
        INVEST["Investigation Engine"]
        AUDIT["Audit Logging"]

        FAST --> EVENT
        FAST --> INCIDENT
        FAST --> INVEST
        FAST --> AUDIT
    end

    subgraph DATA["03  —  DATA LAYER"]
        ORM["SQLAlchemy ORM"]
        DB[("SQLite Database")]
        ORM --> DB
    end

    CLIENT -->|"HTTP / REST"| API
    EVENT --> ORM
    INCIDENT --> ORM
    INVEST --> ORM
    AUDIT --> ORM

    classDef frontend fill:#151D38,stroke:#818CF8,color:#FFFFFF
    classDef backend fill:#102A3D,stroke:#22D3EE,color:#FFFFFF
    classDef database fill:#102F2B,stroke:#34D399,color:#FFFFFF

    class UI,TS,VITE frontend
    class FAST,EVENT,INCIDENT,INVEST,AUDIT backend
    class ORM,DB database
```

### Architecture characteristics

| Area | Implementation |
|---|---|
| Frontend | React + TypeScript |
| Backend | FastAPI |
| API style | REST |
| ORM | SQLAlchemy |
| Database | SQLite |
| Investigation | Deterministic evidence-based engine |
| Testing | Pytest |
| Coverage | Coverage.py |
| Containerization | Docker |

---

# 04 — TECHNOLOGY ECOSYSTEM

<div align="center">

### BUILT WITH A PRACTICAL, MODERN ENGINEERING STACK.

</div>

| Technology | Role in the project |
|---|---|
| Python | Backend development |
| FastAPI | REST API and application layer |
| SQLAlchemy | Database interaction and ORM |
| SQLite | Default persistent storage |
| React | Frontend interface |
| TypeScript | Frontend type safety |
| Vite | Frontend development and build tooling |
| Pytest | Automated backend testing |
| Coverage.py | Test coverage measurement |
| Docker | Containerization support |
| Git & GitHub | Version control and collaboration |

---

# 05 — API REFERENCE

<div align="center">

### A CLEAN REST INTERFACE FOR OPERATIONAL WORKFLOWS.

</div>

**Base URL**

```text
http://127.0.0.1:8000
```

| Method | Endpoint | Responsibility |
|:---:|---|---|
| `GET` | `/health` | Application health check |
| `POST` | `/api/v1/events` | Ingest an operational event |
| `GET` | `/api/v1/events` | Retrieve operational events |
| `GET` | `/api/v1/incidents` | List incidents |
| `POST` | `/api/v1/incidents` | Create an incident |
| `GET` | `/api/v1/incidents/{incident_id}` | Retrieve incident details |
| `POST` | `/api/v1/incidents/{incident_id}/investigate` | Run an investigation |
| `GET` | `/api/v1/incidents/{incident_id}/audit` | Retrieve audit history |

### Interactive API explorer

Once the backend is running, open:

[**Open Swagger API Documentation →**](http://127.0.0.1:8000/docs)

---

# 06 — PROJECT STRUCTURE

```text
opspilot-ai/
│
├── apps/
│   │
│   ├── api/
│   │   └── app/
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
├── data/
│
├── docs/
│   ├── architecture.md
│   ├── data-model.md
│   ├── operations.md
│   └── security.md
│
├── tests/
│   └── test_api.py
│
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 07 — GETTING STARTED

<div align="center">

### YOUR LOCAL OPSPILOT ENVIRONMENT IN A FEW STEPS.

</div>

### Requirements

- Python 3.10+
- Node.js and npm
- Git

### Step 01 — Clone the repository

```bash
git clone https://github.com/akankshad1712/opspilot-ai.git

cd opspilot-ai
```

### Step 02 — Configure the backend

Create a Python virtual environment:

**Windows PowerShell**

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install Python dependencies:

```powershell
pip install -r requirements.txt
```

### Step 03 — Start the backend

From the project root:

```powershell
python -m uvicorn apps.api.app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### Step 04 — Configure the frontend

Open a separate terminal:

```powershell
cd apps/web
```

Install frontend dependencies:

```powershell
npm install
```

Start the frontend:

```powershell
npm run dev
```

Frontend:

```text
http://localhost:5173
```

### Step 05 — Verify the application

Check the health endpoint:

```text
http://127.0.0.1:8000/health
```

Open the frontend and Swagger interface to explore the application.

---

# 08 — TESTING & QUALITY ENGINEERING

<div align="center">

### QUALITY IS MEASURED, NOT ASSUMED.

</div>

OpsPilot AI includes automated backend tests covering the core application workflows.

### Run the test suite

```powershell
python -m pytest -v
```

### Generate coverage results

```powershell
python -m coverage run --branch --source=apps.api.app -m pytest -v

python -m coverage report -m
```

### Verified backend results

<table>
<tr>
<td align="center" width="33%">

# 15

**Passing Tests**

</td>
<td align="center" width="33%">

# 100%

**Statement Coverage**

</td>
<td align="center" width="33%">

# 100%

**Branch Coverage**

</td>
</tr>
</table>

Coverage was measured across the `apps.api.app` backend package.

The test suite covers:

- Health endpoint
- Event ingestion and retrieval
- Incident creation and retrieval
- Investigation workflows
- Related event filtering
- Repeated investigations
- Audit history
- Database session lifecycle

*These coverage figures apply to the backend package, not the React frontend.*

---

# 09 — ENGINEERING PRINCIPLES

| Principle | How OpsPilot AI applies it |
|---|---|
| Evidence First | Investigations use related operational events |
| Deterministic Logic | Current scoring and investigation rules are reproducible |
| Traceability | Audit records preserve investigation activities |
| Modularity | API, frontend, worker, and data concerns are separated |
| Testability | Backend behavior is verified with automated tests |
| Transparency | Findings and confidence are based on explicit signals |

---

# 10 — ROADMAP

<div align="center">

### THE NEXT EVOLUTION OF OPERATIONAL INTELLIGENCE.

</div>

The following are planned enhancements, not features claimed as complete.

```mermaid
flowchart LR
    A["Current MVP"] --> B["Streaming Integration"]
    B --> C["Advanced Observability"]
    C --> D["AI-Assisted Analysis"]
    D --> E["Automated Remediation"]

    classDef current fill:#123A32,stroke:#34D399,color:#FFFFFF
    classDef future fill:#171A30,stroke:#818CF8,color:#FFFFFF

    class A current
    class B,C,D,E future
```

### Planned directions

- [ ] Kafka-based event streaming
- [ ] Redis caching and performance improvements
- [ ] PostgreSQL deployment configuration
- [ ] AI/LLM-assisted incident analysis
- [ ] Advanced observability integrations
- [ ] Authentication and role-based access control
- [ ] Automated incident remediation
- [ ] Expanded frontend and integration tests

---

# 11 — PROJECT DOCUMENTATION

Explore the technical documentation:

| Document | Focus |
|---|---|
| [Architecture](docs/architecture.md) | System architecture |
| [Data Model](docs/data-model.md) | Database structure |
| [Operations](docs/operations.md) | Operational guidance |
| [Security](docs/security.md) | Security considerations |

---

# 12 — ABOUT THE CREATOR

<div align="center">

## AKANKSHA DESHMUKH

### Software Developer | Backend Engineering | Full-Stack Development

Building practical software systems with an interest in backend architecture, APIs, distributed systems concepts, and AI-assisted engineering.

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-akankshad1712-181717?style=for-the-badge&logo=github)](https://github.com/akankshad1712)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Akanksha_Deshmukh-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/akanksha-deshmukh-26210b244)

[![Portfolio](https://img.shields.io/badge/Portfolio-Visit_Website-7C3AED?style=for-the-badge&logo=googlechrome&logoColor=white)](https://akankshadeshmukh.com)

[![LeetCode](https://img.shields.io/badge/LeetCode-Kanksha17-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/Kanksha17/)

</div>

---

<div align="center">

# ◈ OPSPILOT AI

### SEE THE SIGNAL. UNDERSTAND THE INCIDENT. FOLLOW THE EVIDENCE.

**Turning operational complexity into actionable clarity.**

<br/>

Built with curiosity, engineering discipline, and a focus on meaningful software.

<br/>

<sub>© 2026 Akanksha Deshmukh · Licensed under the MIT License</sub>

</div>
