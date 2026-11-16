# 12 — Capacity Planning

Capacity must be measured from actual workload.

## Variables

- events/sec
- average event size
- peak event multiplier
- incidents/day
- AI requests/incident
- prompt/output tokens
- retention period
- database write rate

Approximate daily events:

`events_per_day = average_events_per_second × 86,400`

Storage planning must include indexes, replicas, backups and retention overhead.

Do not claim production capacity until benchmarked.
