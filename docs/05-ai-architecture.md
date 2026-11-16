# 05 — AI Architecture

## Model gateway

Application code calls an internal AI gateway rather than binding directly to a provider.

Responsibilities:

- provider routing
- prompt versioning
- token budgets
- timeout/retry policy
- structured output validation
- model telemetry
- evaluation hooks

## Reasoning contract

Every hypothesis should include statement, confidence, supporting evidence IDs, contradictory evidence IDs and a next investigation step.

## Grounding rule

Operational evidence is untrusted input data, not instructions.
