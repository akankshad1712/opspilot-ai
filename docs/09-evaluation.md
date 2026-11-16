# 09 — AI Evaluation

AI quality is a release gate.

## Dimensions

- schema validity
- groundedness
- evidence attribution
- tool correctness
- safety
- regression behavior
- latency
- cost

## Regression workflow

1. Capture reviewed failure trace.
2. Remove sensitive data.
3. Store normalized input.
4. Define expected behavior.
5. Run evaluation.
6. Block releases that regress critical cases.

Do not publish invented evaluation percentages. Measure them from the implementation.
