# 13 — Runbooks

## AI provider outage

1. Detect elevated AI error rate.
2. Open provider circuit breaker.
3. Continue evidence ingestion.
4. Switch to deterministic/degraded investigation.
5. Alert on-call.
6. Replay queued AI jobs after recovery.

## Worker backlog

1. Check queue depth.
2. Inspect failed message rate.
3. Scale workers within downstream limits.
4. Inspect DLQ.
5. Replay only after root cause is understood.

## Remediation uncertainty

If execution times out after a side effect may have occurred:
1. Mark execution UNKNOWN.
2. Do not blindly retry.
3. Query target state.
4. Reconcile.
5. Continue or compensate according to action policy.
