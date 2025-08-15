from fastapi import FastAPI
from .db import Base, engine
from .routers import items
from .core.config import settings

app = FastAPI(title="FastAPI + Postgres (Poetry) Template")

if settings.RUN_MIGRATIONS:
    Base.metadata.create_all(bind=engine)

@app.get("/health", tags=["system"])
def health():
    return {"status": "ok"}

app.include_router(items.router)
