# Architecture

OpsPilot follows a layered architecture:

1. **Ingestion** — accepts normalized operational events.
2. **Persistence** — stores events and incident state.
3. **Correlation** — groups evidence by service, environment, and time window.
4. **Investigation** — produces a transparent hypothesis from evidence.
5. **Policy** — recommendations are not automatically authorized.
6. **Audit** — important system decisions are recorded.

The current MVP deliberately keeps the AI layer deterministic. A future LLM adapter can receive an evidence bundle and return structured hypotheses, while the application remains responsible for validation and authorization.
