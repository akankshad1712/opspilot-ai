# 07 — Reliability

## Retry

Use retries only for transient failures. Apply exponential backoff and jitter.

## Idempotency

Any externally visible side effect must have an idempotency key.

## Circuit breaker

Downstream AI/integration failures should not cascade into the API.

## Dead-letter queue

Repeatedly failing messages move to a DLQ for inspection and controlled replay.

## Degraded mode

When AI is unavailable, deterministic incident management and evidence collection continue.
