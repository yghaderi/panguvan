import datetime
from typing import Optional
from sqlalchemy import Column, BigInteger
from sqlmodel import SQLModel, Field, UniqueConstraint


class Currency(SQLModel, table=True):
    __tablename__ = "tgju_currency"
    __table_args__ = (
        UniqueConstraint("date", "ins_id", name="tgju_currency_unique_date_symbol"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime.date = Field(foreign_key="date.date")
    symbol: str
    open: int
    high: int
    low: int
    close: int


class Gold(SQLModel, table=True):
    __tablename__ = "tgju_gold"
    __table_args__ = (
        UniqueConstraint("date", "ins_id", name="tgju_gold_unique_date_symbol"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime.date = Field(foreign_key="date.date")
    symbol: str
    open: int = Field(sa_column=Column(BigInteger()))
    high: int = Field(sa_column=Column(BigInteger()))
    low: int = Field(sa_column=Column(BigInteger()))
    close: int = Field(sa_column=Column(BigInteger()))
