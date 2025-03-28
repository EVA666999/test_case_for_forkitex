import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from tronpy import Tron

from app.models.balance import Balance
from app.schemas import BalanceCreateRequest
from app.sqlalchemy.db_depends import get_db

router = APIRouter(prefix="/balance")

MAX_LIMIT = 100


async def pagination_func(limit: int = 10, page: int = 1):
    if limit > MAX_LIMIT:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Limit cannot exceed {MAX_LIMIT}",
        )
    if limit <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Limit must be greater than 0",
        )
    if page <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Page must be greater than 0",
        )
    return {"limit": limit, "page": page}


@router.get("/")
async def get_all_balances(
    db: Annotated[Session, Depends(get_db)], pagination: dict = Depends(pagination_func)
):

    limit = pagination["limit"]
    page = pagination["page"]
    skip = (page - 1) * limit

    get_list = db.scalars(select(Balance).offset(skip).limit(limit)).all()

    return get_list


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_balance(
    db: Annotated[Session, Depends(get_db)], request: BalanceCreateRequest
) -> dict:
    tron_address = request.tron_address

    client = Tron(network="nile")

    balance = client.get_account_balance(tron_address)
    account_info = client.get_account(tron_address)

    bandwidth = account_info["net_window_size"]
    energy = account_info["account_resource"]["energy_window_size"]

    new_balance = Balance(
        tron_address=tron_address, balance=balance, bandwidth=bandwidth, energy=energy
    )

    db.add(new_balance)
    db.commit()

    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}
