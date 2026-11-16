# Remediation Sequence

```text
Investigator → API: approve remediation
API → Policy Engine: evaluate
Policy Engine → API: approval allowed
API → Executor: execute(idempotency_key)
Executor → External System: typed action
External System → Executor: result
Executor → DB: execution + audit
API → Investigator: final status
```
