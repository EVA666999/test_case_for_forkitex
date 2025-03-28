from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.sqlalchemy.db import Base


class Balance(Base):
    __tablename__ = "balances"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    balance: Mapped[float] = mapped_column(Float, nullable=False)
    tron_address: Mapped[str] = mapped_column(String, nullable=False)
    bandwidth: Mapped[int] = mapped_column(Integer, nullable=False)
    energy: Mapped[int] = mapped_column(Integer, nullable=False)
