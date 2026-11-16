# Operations

## Local health

```bash
curl http://localhost:8000/health
```

## Logs

Run the API directly with:

```bash
uvicorn apps.api.app.main:app --reload
```

## Database

SQLite is the default for development. PostgreSQL is supported through `DATABASE_URL`.

## Worker

The worker periodically investigates open incidents:

```bash
python -m apps.worker.main
```

The worker is intentionally simple in this MVP. A production version should use a durable queue such as Kafka, RabbitMQ, SQS, or another appropriate event system.
