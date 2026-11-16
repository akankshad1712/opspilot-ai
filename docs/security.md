# Security

The MVP is intentionally local-first.

## Current controls

- Configuration through environment variables
- No credentials committed to the repository
- CORS configuration
- Evidence and recommendations represented as different objects
- Audit records for ingestion, incident creation, and investigation
- No destructive infrastructure command is executed by the investigation engine

## Production hardening

Before exposing the service publicly:

- Add authentication.
- Add RBAC.
- Add request authentication for event sources.
- Add rate limiting.
- Validate and constrain metadata payloads.
- Use managed secrets.
- Encrypt database traffic.
- Add network policies.
- Add structured authorization for remediation.
- Add immutable or external audit storage.
