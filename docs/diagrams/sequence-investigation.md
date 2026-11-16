# Investigation Sequence

```text
Client → API: investigate incident
API → DB: load incident
API → Evidence: fetch correlated evidence
API → AI Gateway: structured investigation request
AI Gateway → Model: prompt + evidence
Model → AI Gateway: structured result
AI Gateway → API: validated result
API → DB: persist hypotheses
API → Client: investigation result
```
