# OpsPilot AI — Evidence-Driven Operations Intelligence Platform

**Author:** Akanksha Deshmukh  
**Email:** akankshadeshmukh308@gmail.com  
**Status:** Portfolio architecture / reference implementation blueprint  
**Positioning:** AI Engineering • Backend Systems • Reliability • Observability • Human-in-the-Loop

> OpsPilot AI is a production-oriented platform concept for turning fragmented operational signals—application logs, API failures, support tickets, deployment events, and service metrics—into traceable incident investigations and controlled remediation workflows.

This repository is intentionally designed to demonstrate **systems thinking**, not merely an LLM API call. Every AI conclusion is connected to evidence, every automated action is policy-controlled, and every important transition is auditable.

## 1. Why OpsPilot AI?

Operational teams rarely receive a clean description of an incident. They receive fragments: 5xx spikes, a recent deployment, database latency, noisy logs, alerts, and support tickets. OpsPilot correlates these signals into a structured investigation.

**Core objective:**

`Signal → Correlation → Evidence → AI Reasoning → Human Approval → Safe Action → Audit`

The model proposes; deterministic policy and humans control consequential execution.

## 2. Design Principles

1. Evidence before explanation.
2. Deterministic boundaries around probabilistic AI.
3. Human approval for consequential actions.
4. Idempotent operations.
5. Observable by default.
6. Failure-aware architecture.
7. Security by design.
8. Reproducible AI evaluation.
9. Modular AI providers.
10. Clear separation of control plane and data plane.

## 3. High-Level Architecture

```text
Clients
   │ HTTPS
   ▼
API Gateway ── Auth / RBAC / Rate Limit
   │
   ▼
Incident Service ───────────────► PostgreSQL
   │                                  ▲
   ├── Event Ingestion → Kafka → Correlation Workers
   │                                  │
   └── Investigation → AI Gateway ← Evidence Store
                              │
                              ▼
                       Policy / Guardrails
                              │
                       Human Approval
                              │
                              ▼
                     Remediation Executor
                              │
                              ▼
                      External Systems
                              │
                              ▼
                         Audit Trail
```

## 4. Repository Structure

```text
opspilot-ai/
├── README.md
├── SECURITY.md
├── .env.example
├── .gitignore
├── docker-compose.yml
├── docs/
│   ├── README.md
│   ├── 00-overview.md
│   ├── 01-requirements.md
│   ├── 02-system-design.md
│   ├── 03-data-model.md
│   ├── 04-api-contracts.md
│   ├── 05-ai-architecture.md
│   ├── 06-security.md
│   ├── 07-reliability.md
│   ├── 08-observability.md
│   ├── 09-evaluation.md
│   ├── 10-adr.md
│   ├── 11-threat-model.md
│   ├── 12-capacity-planning.md
│   ├── 13-runbooks.md
│   └── diagrams/
│       ├── architecture.md
│       ├── sequence-investigation.md
│       └── sequence-remediation.md
├── apps/
│   ├── api/
│   ├── worker/
│   ├── ai_gateway/
│   └── web/
├── packages/
│   ├── domain/
│   ├── contracts/
│   ├── policies/
│   └── telemetry/
├── infrastructure/
│   ├── docker/
│   ├── postgres/
│   ├── kafka/
│   └── github-actions/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── contract/
│   ├── evaluation/
│   └── e2e/
├── scripts/
│   └── replay_incident.py
└── data/
    └── demo/
```

## 5. Suggested Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| API | Python + FastAPI | typed service boundary |
| Database | PostgreSQL | transactional source of truth |
| Cache | Redis | caching, locks, rate limiting |
| Events | Kafka | durable async processing |
| AI | Gemini / compatible LLM API | structured reasoning |
| Frontend | React + TypeScript | investigator console |
| Auth | JWT/OAuth2 | identity |
| Containers | Docker | reproducible deployment |
| CI/CD | GitHub Actions | automated validation |
| Observability | OpenTelemetry | traces/metrics/log correlation |
| Testing | Pytest | unit/integration/evaluation |
| Contracts | OpenAPI + JSON Schema | API/model boundaries |

## 6. Domain Model

**Incident:** operational problem and lifecycle state.

**Evidence:** immutable source material used in investigation, including source type, source ID, timestamp, content hash, and metadata.

**Hypothesis:** possible explanation with supporting/contradictory evidence IDs and confidence.

**Remediation:** typed operational action with risk, policy decision, approval and idempotency key.

**AuditEvent:** append-only security/operational record.

## 7. Core Tables

### incidents

| Column | Type | Notes |
|---|---|---|
| id | UUID | Primary key |
| title | TEXT | Incident title |
| severity | ENUM | SEV1–SEV4 |
| status | ENUM | OPEN / INVESTIGATING / MITIGATED / RESOLVED |
| service | TEXT | Affected service |
| detected_at | TIMESTAMP | Detection time |
| resolved_at | TIMESTAMP | Nullable |
| correlation_id | UUID | Trace/correlation |
| created_at | TIMESTAMP | Creation timestamp |

### evidence

| Column | Type | Notes |
|---|---|---|
| id | UUID | Primary key |
| incident_id | UUID | Foreign key |
| source_type | TEXT | log/metric/ticket/deploy |
| source_id | TEXT | Source identifier |
| observed_at | TIMESTAMP | Event time |
| content | JSONB | Normalized payload |
| content_hash | TEXT | Deduplication/integrity |
| relevance_score | NUMERIC | Ranking |
| created_at | TIMESTAMP | Ingestion time |

### hypotheses

| Column | Type | Notes |
|---|---|---|
| id | UUID | Primary key |
| incident_id | UUID | Foreign key |
| statement | TEXT | Hypothesis |
| confidence | NUMERIC | 0–1 |
| status | TEXT | PROPOSED / ACCEPTED / REJECTED |
| created_at | TIMESTAMP | Generation time |

### remediations

| Column | Type | Notes |
|---|---|---|
| id | UUID | Primary key |
| incident_id | UUID | Foreign key |
| action_type | TEXT | Typed action |
| parameters | JSONB | Validated arguments |
| risk_level | TEXT | LOW / MEDIUM / HIGH |
| policy_decision | TEXT | ALLOW / DENY / APPROVAL_REQUIRED |
| approval_id | UUID | Nullable |
| idempotency_key | TEXT | Unique |
| execution_status | TEXT | PENDING / RUNNING / SUCCESS / FAILED |

### audit_events

| Column | Type | Notes |
|---|---|---|
| id | UUID | Primary key |
| actor_id | UUID | User/service |
| action | TEXT | Action performed |
| resource_type | TEXT | Resource category |
| resource_id | UUID | Target |
| request_id | UUID | Request correlation |
| result | TEXT | SUCCESS / FAILURE |
| metadata | JSONB | Context |
| created_at | TIMESTAMP | Append-only |

## 8. Investigation Lifecycle

```text
DETECTED
   ↓
TRIAGED
   ↓
EVIDENCE_COLLECTED
   ↓
CORRELATED
   ↓
AI_ANALYSIS
   ├── insufficient evidence → REQUEST_MORE_DATA
   ↓
HYPOTHESES_GENERATED
   ↓
HUMAN_REVIEW
   ├── rejected → INVESTIGATING
   ↓
REMEDIATION_PROPOSED
   ↓
POLICY_CHECK
   ├── denied → CLOSED_WITHOUT_ACTION
   ├── approval required → HUMAN_APPROVAL
   ↓
EXECUTION
   ├── failed → ROLLBACK / ESCALATE
   ↓
VERIFICATION
   ↓
RESOLVED
   ↓
POST_INCIDENT_REPORT
```

## 9. AI Architecture

The LLM is **not** the system of record.

### AI responsibilities

- summarize evidence
- classify incident type
- identify patterns
- propose root-cause hypotheses
- rank investigation paths
- draft incident reports
- recommend typed remediation

### Non-AI responsibilities

- authentication
- authorization
- persistence
- state transitions
- policy enforcement
- idempotency
- execution
- audit logging

### Structured contract

```json
{
  "incident_summary": "...",
  "hypotheses": [
    {
      "statement": "...",
      "confidence": 0.0,
      "supporting_evidence_ids": [],
      "contradictory_evidence_ids": []
    }
  ],
  "next_investigation_steps": [],
  "recommended_remediation": {
    "action_type": "...",
    "risk_level": "LOW|MEDIUM|HIGH"
  }
}
```

The API validates this structure before it enters the domain layer.

## 10. Evidence-First Reasoning

Every model request receives:

1. incident metadata
2. normalized evidence
3. explicit evidence IDs
4. known constraints
5. required output schema
6. instruction to distinguish facts from hypotheses
7. instruction to identify missing evidence

Operational evidence is treated as **untrusted data**, never as executable instructions.

## 11. Evaluation

AI quality is a release gate.

| Dimension | Example |
|---|---|
| Groundedness | Claims supported by evidence |
| Schema validity | Valid structured output |
| Evidence attribution | Correct evidence IDs |
| Tool correctness | Correct action selection |
| Safety | No unauthorized remediation |
| Regression | Known incidents remain correct |
| Consistency | Similar incidents remain stable |
| Latency | Within SLO |
| Cost | Within budget |

Reviewed production-like failures can become regression cases. Do not publish evaluation percentages until they have actually been measured.

## 12. Observability

Three telemetry layers:

**Metrics:** request rate, error rate, p95/p99 latency, queue depth, worker failures, AI latency/tokens, remediation success.

**Logs:** structured JSON with timestamp, level, service, request_id, trace_id, incident_id, actor_id, event and error_code.

**Traces:** HTTP → incident service → evidence query → correlation → AI gateway → validation → policy → remediation.

Observability is especially important for AI workflows because a healthy API can still hide an incorrect tool call or unsupported model conclusion.

## 13. Reliability

### Retry

Use retries only for transient failures, with exponential backoff and jitter.

### Circuit breaker

External providers can move through CLOSED → OPEN → HALF_OPEN.

### Idempotency

Every remediation command carries an idempotency key. Repeated requests return the original execution result instead of duplicating the side effect.

### Dead-letter queue

Repeatedly failing messages move to a DLQ for controlled inspection/replay.

### Degraded mode

AI unavailability must not stop evidence ingestion and deterministic incident management.

## 14. Security

Roles:

| Role | Read | Investigate | Approve | Execute | Admin |
|---|---:|---:|---:|---:|---:|
| Viewer | ✓ | | | | |
| Investigator | ✓ | ✓ | | | |
| Approver | ✓ | ✓ | ✓ | | |
| Operator | ✓ | ✓ | ✓ | ✓ | |
| Admin | ✓ | ✓ | ✓ | ✓ | ✓ |

Controls include authentication, RBAC, least privilege, rate limiting, secret management, request validation, audit logging, evidence integrity and allowlisted remediation.

## 15. Safe Remediation

Never expose arbitrary shell execution to an LLM. Use typed actions:

```text
RestartService(service_id)
RollbackDeployment(deployment_id)
ScaleService(service_id, desired_replicas)
OpenTicket(ticket_payload)
NotifyOnCall(team_id)
```

Each action has a schema, authorization requirement, risk class, timeout, retry behavior, audit event and rollback strategy where possible.

## 16. API Surface

```text
POST   /v1/incidents
GET    /v1/incidents/{id}
GET    /v1/incidents/{id}/timeline
POST   /v1/incidents/{id}/investigate
POST   /v1/incidents/{id}/evidence
POST   /v1/incidents/{id}/hypotheses
POST   /v1/incidents/{id}/remediations
POST   /v1/remediations/{id}/approve
POST   /v1/remediations/{id}/execute
GET    /v1/audit
GET    /v1/incidents/{id}/audit
```

Stable machine-readable error codes should be used by clients.

## 17. Scaling

- Stateless API replicas.
- Independent worker replicas.
- Kafka partitions for throughput and ordering boundaries.
- PostgreSQL read replicas when justified by measurements.
- Redis for bounded caching/coordination.
- Backpressure and bounded concurrency to protect downstream systems.

Capacity must be benchmarked before making production performance claims.

## 18. Cost Controls

Use model routing, prompt minimization, evidence ranking, caching, token budgets and smaller models for simple classification. Reserve high-capability models for complex investigations.

```text
Simple classification → fast/small model
Evidence extraction   → structured model
Complex RCA           → high-capability model
Provider unavailable  → deterministic fallback
```

## 19. Human-in-the-Loop

```text
AI recommendation
       ↓
Risk classification
       ↓
Policy engine
       ├── low-risk + allowed
       └── medium/high-risk
                 ↓
            Human approval
                 ↓
              Execution
```

The investigator should see the evidence, uncertainty, confidence, recommended action, risk and approval requirement—not only a generated answer.

## 20. Engineering Quality Gates

A pull request should pass:

- formatting
- linting
- type checking
- unit tests
- integration tests
- contract tests
- security checks
- AI evaluation suite
- migration validation
- container build
- dependency audit

## 21. Testing Pyramid

```text
              E2E
               ▲
        Integration / Contract
               ▲
          Unit / Domain
               ▲
       AI Safety / Evaluation
```

Test domain logic, API validation, transactions, authorization, idempotency, evidence grounding, prompt-injection resistance and remediation safety.

## 22. Portfolio Demo

A strong demonstration should show one complete incident:

1. Create incident.
2. Ingest logs, deployment event and metric anomaly.
3. Correlate evidence.
4. Run AI investigation.
5. Display evidence-backed hypotheses.
6. Generate typed remediation.
7. Show policy decision.
8. Approve action.
9. Execute remediation.
10. Verify recovery.
11. Display audit timeline.
12. Generate post-incident report.

This demonstrates an end-to-end engineering system rather than a standalone chatbot.

## 23. Senior-Level Engineering Signal

The differentiator is the engineering around the model:

- distributed event processing
- domain-driven state
- evidence lineage
- deterministic policy enforcement
- human approval
- idempotency
- failure handling
- observability
- evaluation
- security
- cost controls
- auditability
- reproducibility

A serious AI system should answer not only **“What did the model say?”** but also **“Why? What evidence supports it? What happened when it was wrong? Who approved the action? Can we reproduce the decision? Can we safely recover?”**

## 24. Author

**Akanksha Deshmukh**  
AI Software Engineer / Backend Engineer  
Pune, Maharashtra, India  
akankshadeshmukh308@gmail.com

> This repository is a design/implementation blueprint until the corresponding code, tests and measurements are actually built. Never claim unimplemented architecture, benchmark results, uptime or evaluation scores as completed achievements.

## Reference context

This architecture is aligned with the MHTECHIN Junior AI Engineer role's emphasis on AI applications, APIs, automation, data processing, AI integration, testing, databases and version control. citeturn952469search0

Current AI engineering practice also increasingly emphasizes production reliability, observability and evaluation for AI systems. citeturn952469search4turn952469search9
