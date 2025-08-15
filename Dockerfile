FROM python:3.12-slim

ENV POETRY_VERSION=1.8.3     POETRY_VIRTUALENVS_CREATE=false     PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends     build-essential curl &&     pip install --no-cache-dir "poetry==$POETRY_VERSION" &&     rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root --no-interaction --no-ansi

COPY . .

EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
