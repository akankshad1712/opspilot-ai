# 11 — Threat Model

## Assets

- operational logs
- incident metadata
- credentials
- remediation controls
- audit records
- AI provider credentials

## Threats

T1 Prompt injection  
T2 Credential leakage  
T3 Unauthorized remediation  
T4 Replay/duplicate execution  
T5 Evidence tampering  
T6 Denial of service  
T7 Data exfiltration

## Mitigations

Untrusted-data boundaries, secrets management, RBAC, idempotency, evidence hashes, rate limits, redaction and immutable audit events.
