# 03 — Data Model

Core entities:

- Incident
- Evidence
- Hypothesis
- Remediation
- Approval
- AuditEvent
- DeploymentEvent
- MetricObservation
- SupportTicket

PostgreSQL is the transactional source of truth. Long-running work is asynchronous.

Evidence receives a content hash for deduplication/integrity. Remediation execution uses an idempotency key with a unique constraint.
