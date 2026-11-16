# Data Model

## Event

Represents an operational observation.

- source
- service
- environment
- timestamp
- severity
- message
- metadata

## Incident

Represents an operational problem being investigated.

- title
- service
- environment
- started_at
- status

## Investigation

Represents a derived analysis.

- summary
- confidence
- evidence_count
- hypothesis
- recommendation

## AuditLog

Represents a trace of system decisions.

- incident_id
- action
- actor
- detail
- created_at
