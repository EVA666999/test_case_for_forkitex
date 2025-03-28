import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.sqlalchemy.db import Base, SessionLocal, engine


@pytest.fixture
def client():
    return TestClient(app)
