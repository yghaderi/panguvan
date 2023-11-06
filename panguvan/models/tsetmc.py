import datetime
from typing import Optional
from sqlalchemy import Column, BigInteger
from sqlmodel import SQLModel, Field, UniqueConstraint


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
    __tablename__ = "tsetmc_economic_sector"

    id: int = Field(primary_key=True)
    name: str


class BusinessSector(SQLModel, table=True):
    __tablename__ = "tsetmc_business_sector"

    id: int = Field(primary_key=True)
    name: str
    economic_sector_id: int = Field(foreign_key="tsetmc_economic_sector.id")


class IndustryGroup(SQLModel, table=True):
    __tablename__ = "tsetmc_industry_group"

    id: int = Field(primary_key=True)
    name: str
    business_sector_id: int = Field(foreign_key="tsetmc_business_sector.id")


class Industry(SQLModel, table=True):
    __tablename__ = "tsetmc_industry"

    id: int = Field(primary_key=True)
    name: str
    industry_group_id: int = Field(foreign_key="tsetmc_industry_group.id")


class Activity(SQLModel, table=True):
    __tablename__ = "tsetmc_activity"

    id: int = Field(sa_column=Column(BigInteger(), primary_key=True))
    name: str
    industry_id: int = Field(foreign_key="tsetmc_industry.id")


class Market(SQLModel, table=True):
    __tablename__ = "tsetmc_market"

    id: int = Field(primary_key=True)
    name: str


class Instrument(SQLModel, table=True):
    __tablename__ = "tsetmc_instrument"

    ins_id: str = Field(primary_key=True)
    ins_code: int = Field(sa_column=Column(BigInteger()))
    symbol: str
    name: str
    symbol_en: str
    name_en: str

    activity_id: int = Field(
        sa_column=Column(BigInteger()), foreign_key="tsetmc_activity.id"
    )
    market_id: int = Field(foreign_key="tsetmc_market.id")


class DailyHistPrice(SQLModel, table=True):
    __tablename__ = "tsetmc_daily_hist_price"
    __table_args__ = (
        UniqueConstraint(
            "date", "ins_id", name="tsetmc_daily_hist_price_unique_date_ins_id"
        ),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime.date = Field(foreign_key="date.date")
    ins_id: str = Field(foreign_key="tsetmc_instrument.ins_id")
    open: int
    high: int
    low: int
    close: int
    final: int
    y_final: Optional[int] = Field(default=None)
    volume: int = Field(sa_column=Column(BigInteger()))
    value: int = Field(sa_column=Column(BigInteger()))
    trade_count: int = Field(sa_column=Column(BigInteger()))


class DailyAdjHistPrice(SQLModel, table=True):
    __tablename__ = "tsetmc_daily_adj_hist_price"
    __table_args__ = (
        UniqueConstraint(
            "date", "ins_id", name="tsetmc_daily_adj_hist_price_unique_date_ins_id"
        ),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime.date = Field(foreign_key="date.date")
    ins_id: str = Field(foreign_key="tsetmc_instrument.ins_id")
    open: int
    high: int
    low: int
    close: int
    final: int
    volume: int = Field(sa_column=Column(BigInteger()))
    value: int = Field(sa_column=Column(BigInteger()))
    trade_count: int = Field(sa_column=Column(BigInteger()))


class OptionInfo(SQLModel, table=True):
    __tablename__ = "tsetmc_option_info"

    id: Optional[int] = Field(default=None, primary_key=True)
    ins_id: str = Field(primary_key=True)
    listed_date: datetime.date
    ex_date: datetime.date
    lot_size: int
    k: int


class OptionHistPrice(SQLModel, table=True):
    __tablename__ = "tsetmc_option_hist_price"
    __table_args__ = (
        UniqueConstraint(
            "date", "ins_id", name="tsetmc_daily_adj_hist_price_unique_date_ins_id"
        ),
    )
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime.date = Field(foreign_key="date.date")
    ins_id: str = Field(foreign_key="tsetmc_instrument.ins_id")
    open: int
    high: int
    low: int
    close: int
    final: int
    volume: int = Field(sa_column=Column(BigInteger()))
    value: int = Field(sa_column=Column(BigInteger()))
    trade_count: int = Field(sa_column=Column(BigInteger()))
    open_interest: int = Field(sa_column=Column(BigInteger()))
