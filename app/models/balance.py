from app.sqlalchemy.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Boolean, DateTime



class Balance(Base):
    __tablename__ = "balances"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    balance: Mapped[float] = mapped_column(Float, nullable=False)
    tron_address: Mapped[str] = mapped_column(String, nullable=False)
    bandwidth: Mapped[int] = mapped_column(Integer, nullable=False)
    energy: Mapped[int] = mapped_column(Integer, nullable=False)
