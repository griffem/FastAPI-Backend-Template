import os
os.environ["RUN_MIGRATIONS"] = "False"

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app import models
from app.db import Base
from app.deps import get_db

engine = create_engine(
    "sqlite+pysqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base.metadata.create_all(bind=engine)

with TestingSessionLocal() as db:
    db.add(models.Item(name="Hello World"))
    db.commit()

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_list_items_get():
    r = client.get("/items/")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert any(item["name"] == "Hello World" for item in data)
