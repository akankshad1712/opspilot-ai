# Architecture Diagram

```text
Clients
  │
  ▼
API Gateway
  │
  ▼
Incident Service ───────► PostgreSQL
  │
  ├────► Event Bus ─────► Correlation Workers
  │                         │
  │                         ▼
  └────► AI Gateway ◄──── Evidence Store
              │
              ▼
        Policy Engine
              │
       approval required
              ▼
       Remediation Executor
              │
              ▼
        External Systems
```
