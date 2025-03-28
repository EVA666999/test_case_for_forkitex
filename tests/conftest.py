from fastapi.testclient import TestClient
from app.main import app
import pytest


from app.sqlalchemy.db import Base, engine, SessionLocal

@pytest.fixture
def client():
    return TestClient(app)
