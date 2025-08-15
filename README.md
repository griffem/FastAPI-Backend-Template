# FastAPI + Postgres (Poetry) Template

Minimal, reusable template with:
- FastAPI + SQLAlchemy
- Postgres (psycopg)
- `/health` and `/items/` (GET)
- Pytest with in-memory SQLite override
- Poetry for deps & scripts (`poe` tasks)
- Dockerfile + docker-compose
- `.env` via `pydantic-settings`
- Ruff/Black/Mypy pre-configured

## Quickstart

```bash
# Install Poetry (https://python-poetry.org/docs/)
poetry install
cp .env.example .env

# (optional) Start Postgres
docker compose up -d db

# Run the API
poetry run poe run
# -> http://127.0.0.1:8000/docs
```

## Tests
```bash
poetry run poe test
```

## Lint/Format/Type-check
```bash
poetry run poe lint
poetry run poe fmt
poetry run poe typecheck
```

## Docker (API + DB)
```bash
docker compose up --build
```
