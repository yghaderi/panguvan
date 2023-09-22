from collections import namedtuple
import datetime
from typing import Optional
from sqlalchemy import Column, BigInteger
from sqlmodel import SQLModel, Field, UniqueConstraint

from ..engin import conn_engine

ISE = namedtuple("ISE", ["create_tables", "drop_tables"])


class Date(SQLModel, table=True):
    __tablename__ = "date"

    date: datetime.date = Field(primary_key=True)
    jdate: str
    jyear: int
    jmonth: int
    jquarter: int
    jday: int
    jweek_day: int
    jweek_number: int


class EconomicSector(SQLModel, table=True):
    __tablename__ = "ise_economic_sector"

    id: int = Field(primary_key=True)
    name: str


class BusinessSector(SQLModel, table=True):
    __tablename__ = "ise_business_sector"

    id: int = Field(primary_key=True)
    name: str
    economic_sector_id: int = Field(foreign_key="ise_economic_sector.id")


class IndustryGroup(SQLModel, table=True):
    __tablename__ = "ise_industry_group"

    id: int = Field(primary_key=True)
    name: str
    business_sector_id: int = Field(foreign_key="ise_business_sector.id")


class Industry(SQLModel, table=True):
    __tablename__ = "ise_industry"

    id: int = Field(primary_key=True)
    name: str
    industry_group_id: int = Field(foreign_key="ise_industry_group.id")


class Activity(SQLModel, table=True):
    __tablename__ = "ise_activity"

    id: int = Field(sa_column=Column(BigInteger(), primary_key=True))
    name: str
    industry_id: int = Field(foreign_key="ise_industry.id")


class Market(SQLModel, table=True):
    __tablename__ = "ise_market"

    id: int = Field(primary_key=True)
    name: str


class Instrument(SQLModel, table=True):
    __tablename__ = "ise_instrument"

    ins_id: str = Field(primary_key=True)
    ins_code: int = Field(sa_column=Column(BigInteger()))
    symbol: str
    name: str
    symbol_en: str
    name_en: str

    activity_id: int = Field(
        sa_column=Column(BigInteger()), foreign_key="ise_activity.id"
    )
    market_id: int = Field(foreign_key="ise_market.id")


class DailyHistPrice(SQLModel, table=True):
    __tablename__ = "ise_daily_hist_price"
    __table_args__ = (
        UniqueConstraint(
            "date", "ins_id", name="ise_daily_hist_price_unique_date_ins_id"
        ),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime.date = Field(foreign_key="date.date")
    ins_id: str = Field(foreign_key="ise_instrument.ins_id")
    open: int
    high: int
    low: int
    close: int
    final: Optional[int] = Field(default=None)
    y_final: Optional[int] = Field(default=None)
    volume: int = Field(sa_column=Column(BigInteger()))
    value: int = Field(sa_column=Column(BigInteger()))


class DailyAdjHistPrice(SQLModel, table=True):
    __tablename__ = "ise_daily_adj_hist_price"
    __table_args__ = (
        UniqueConstraint(
            "date", "ins_id", name="ise_daily_adj_hist_price_unique_date_ins_id"
        ),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime.date = Field(foreign_key="date.date")
    ins_id: str = Field(foreign_key="ise_instrument.ins_id")
    open: int
    high: int
    low: int
    close: int
    final: Optional[int] = Field(default=None)
    volume: int = Field(sa_column=Column(BigInteger()))
    value: int = Field(sa_column=Column(BigInteger()))


def create_tables():
    engine = conn_engine()
    SQLModel.metadata.create_all(engine)


def drop_tables():
    engine = conn_engine()
    SQLModel.metadata.drop_all(engine)


ise = ISE(create_tables=create_tables, drop_tables=drop_tables)
