# FastAPI + Postgres (Poetry) Template

Minimal, reusable template with:
- FastAPI + SQLAlchemy 2.0
- Postgres (psycopg 3)
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

## Reuse this as a template

**Option A: GitHub Template**
1. Push this folder to a new GitHub repo.
2. In repo Settings → *Template repository* → enable.
3. Click **Use this template** whenever you start a project.

**Option B: Copier (advanced)**
1. `pipx install copier`
2. Convert static values (name, description, module path) to Jinja variables and add `copier.yml`.
3. Generate new projects with: `copier copy gh:your/repo new-project`

**Option C: Cookiecutter**
1. `pipx install cookiecutter`
2. Replace static fields with cookiecutter variables in filenames and `pyproject.toml`.
3. `cookiecutter gh:your/repo`

> Start simple with Option A. Move to Copier/Cookiecutter if you want interactive prompts and updatable templates.
