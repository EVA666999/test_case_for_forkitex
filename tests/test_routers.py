import os

from dotenv import load_dotenv
from fastapi import status
from fastapi.testclient import TestClient

from app.main import app
from app.models.balance import Balance
from app.sqlalchemy.db import Base, SessionLocal, engine

load_dotenv()

client = TestClient(app)


def setup_db():
    Base.metadata.create_all(bind=engine)
    return SessionLocal()


def test_create_balance():
    db = setup_db()
    test_data = {"tron_address": os.getenv("TRONADDRESS")}

    response = client.post("/balance", json=test_data)
    # print(response.json())
    assert response.status_code == 201
    balance = (
        db.query(Balance)
        .filter(Balance.tron_address == test_data["tron_address"])
        .first()
    )
    assert balance is not None
    assert balance.tron_address == test_data["tron_address"]

    db.close()


def test_get_balance():
    response = client.get("/balance")
    assert response.status_code == status.HTTP_200_OK
