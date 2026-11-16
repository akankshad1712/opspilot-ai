# 02 — System Design

## Architecture boundaries

### API layer
HTTP, authentication, validation and response contracts.

### Domain layer
Incident state, investigation workflow and remediation rules.

### Event layer
Ingestion, normalization, deduplication and asynchronous processing.

### AI gateway
Model-provider abstraction, structured output, budgets and telemetry.

### Policy layer
Authorization and risk decisions independently from the model.

### Execution layer
Typed, allowlisted operational actions only.

### Audit layer
Security and operational state-transition records.

## Critical rule

The LLM can recommend a remediation but cannot directly invoke arbitrary infrastructure commands.
