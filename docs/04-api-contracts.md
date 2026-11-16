# 04 — API Contracts

All APIs should expose OpenAPI documentation.

## Incident

POST /v1/incidents
GET /v1/incidents/{id}
GET /v1/incidents/{id}/timeline
POST /v1/incidents/{id}/investigate
POST /v1/incidents/{id}/evidence

## Remediation

POST /v1/incidents/{id}/remediations
POST /v1/remediations/{id}/approve
POST /v1/remediations/{id}/execute

## Error contract

```json
{
  "error": {
    "code": "STABLE_MACHINE_READABLE_CODE",
    "message": "Human-readable explanation.",
    "request_id": "uuid",
    "details": {}
  }
}
```
