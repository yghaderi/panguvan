import datetime
from typing import Optional
import enum
from sqlmodel import SQLModel, MetaData, Field, Enum, UniqueConstraint
from sqlalchemy import Column, BigInteger


class Instrument(SQLModel, table=True):
    __tablename__ = "instrument"

    id: str = Field(primary_key=True) # symbol
    name: str = Field(unique_items=True)
    category: str

    __table_args__ = {"schema": "tgju"}

class HistPrice(SQLModel, table=True):
    __tablename__ = "hist_price"

    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime.date
    symbol: str = Field(foreign_key="tgju.instrument.id")
    open: int = Field(sa_column=Column(BigInteger()))
    high: int = Field(sa_column=Column(BigInteger()))
    low: int = Field(sa_column=Column(BigInteger()))
    close: int = Field(sa_column=Column(BigInteger()))

    __table_args__ = (
        UniqueConstraint("date", "symbol", name="hist_price_unique_date_symbol"),{"schema": "tgju"}
    )
