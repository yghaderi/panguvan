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
    __tablename__ = "ise_economic_sector"

    id: int = Field(primary_key=True)
    name: str = Field(unique=True)


class BusinessSector(SQLModel, table=True):
    __tablename__ = "ise_business_sector"

    id: int = Field(primary_key=True)
    name: str = Field(unique=True)
    economic_sector_id: int = Field(foreign_key="ise_economic_sector.id")


class IndustryGroup(SQLModel, table=True):
    __tablename__ = "ise_industry_group"

    id: int = Field(primary_key=True)
    name: str = Field(unique=True)
    business_sector_id: int = Field(foreign_key="ise_business_sector.id")


class Industry(SQLModel, table=True):
    __tablename__ = "ise_industry"

    id: int = Field(primary_key=True)
    name: str = Field(unique=True)
    industry_group_id: int = Field(foreign_key="ise_industry_group.id")


class Activity(SQLModel, table=True):
    __tablename__ = "ise_activity"

    id: int = Field(sa_column=Column(BigInteger(), primary_key=True))
    name: str = Field(unique=True)
    industry_id: int = Field(foreign_key="ise_industry.id")


class Market(SQLModel, table=True):
    __tablename__ = "ise_market"

    id: int = Field(primary_key=True)
    name: str = Field(unique=True)


class Stocks(SQLModel, table=True):
    __tablename__ = "ise_stocks"

    ins_id: str = Field(primary_key=True)
    ins_code: int = Field(sa_column=Column(BigInteger()))
    symbol: str = Field(unique=True)
    name: str
    symbol_en: str
    name_en: str

    activity_id: int = Field(
        sa_column=Column(BigInteger()), foreign_key="ise_activity.id"
    )
    market_id: int = Field(foreign_key="ise_market.id")


class StockDailyHistTrade(SQLModel, table=True):
    __tablename__ = "ise_stock_daily_hist_trade"
    __table_args__ = (
        UniqueConstraint(
            "date", "ins_id", name="ise_stock_daily_hist_trade_unique_date_ins_id"
        ),
    )

    id: int = Field(default=None, primary_key=True)
    date: datetime.date = Field(foreign_key="date.date")
    ins_id: str = Field(foreign_key="ise_stocks.ins_id")
    open: int
    high: int
    low: int
    close: int
    final: int
    y_final: Optional[int] = Field(default=None)
    volume: int = Field(sa_column=Column(BigInteger()))
    value: int = Field(sa_column=Column(BigInteger()))
    trade_count: int = Field(sa_column=Column(BigInteger()))


class StockDailyAdjHistTrade(SQLModel, table=True):
    __tablename__ = "ise_stock_daily_adj_hist_trade"
    __table_args__ = (
        UniqueConstraint(
            "date", "ins_id", name="ise_daily_adj_hist_trade_unique_date_ins_id"
        ),
    )

    id: int = Field(default=None, primary_key=True)
    date: datetime.date = Field(foreign_key="date.date")
    ins_id: str = Field(foreign_key="ise_stocks.ins_id")
    open: int
    high: int
    low: int
    close: int
    final: int
    volume: int = Field(sa_column=Column(BigInteger()))
    value: int = Field(sa_column=Column(BigInteger()))
    trade_count: int = Field(sa_column=Column(BigInteger()))


class Options(SQLModel, table=True):
    __tablename__ = "ise_options"

    id: int = Field(default=None, primary_key=True)
    ins_id: str = Field(unique=True)
    ins_code: str = Field(unique=True)
    ua_ins_code: str
    symbol: str
    name: str
    type: str
    listed_date: datetime.date
    ex_date: datetime.date


class OptionDailyHistTrade(SQLModel, table=True):
    __tablename__ = "ise_option_daily_hist_trade"
    __table_args__ = (
        UniqueConstraint(
            "date", "ins_id", name="ise_option_daily_hist_trade_unique_date_ins_id"
        ),
    )
    id: int = Field(default=None, primary_key=True)
    date: datetime.date = Field(foreign_key="date.date")
    ins_id: str = Field(foreign_key="ise_options.ins_id")
    open: int
    high: int
    low: int
    close: int
    final: int
    volume: int = Field(sa_column=Column(BigInteger()))
    value: int = Field(sa_column=Column(BigInteger()))
    trade_count: int = Field(sa_column=Column(BigInteger()))
    open_interest: int = Field(sa_column=Column(BigInteger()))
    k: int
    t: int
    lot_size: int
