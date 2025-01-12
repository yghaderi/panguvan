from dagster import asset
import polars as pl
from sqlalchemy.future import select
from sqlalchemy import func
from oxtapus import TGJU

from iceberg.db import async_session
from igloo.tgju import Instrument, HistPrice

tgju_ = TGJU()

async def get_last_date(symbol:str):
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(func.max(HistPrice.date)).where(HistPrice.symbol==symbol))
            max_date = result.scalar()
            return max_date


async def insert_df(df:pl.DataFrame):
    max_date = await get_last_date(df["symbol"][0])
    if max_date:
        df = df.filter(pl.col("date")> max_date)
    if not df.is_empty():
        async with async_session() as session:
            async with session.begin():
                records = [HistPrice(**i) for i in df.to_dicts()]
                session.add_all(records)
                await session.commit()


@asset
async def add_instrument():
    async with async_session() as session:
        async with session.begin():
            records = [
                Instrument(
                id="USDIRR", name="دلار", category="currency"
            ),
            Instrument(
            id="EMAMI", name="سکه‌یِ امامی", category="gold"
        ),
        Instrument(
        id="XAUUSD", name="انسِ طلا", category="gold"
    ),
            ]
            session.add_all(records)
            await session.commit()

@asset
async def update_usd_irr():
    df = tgju_.usd_irr()
    df = df.drop("jdate").with_columns(symbol = pl.lit("USDIRR"))
    await insert_df(df)

@asset
async def update_sekke_emami():
    df = tgju_.sekke_emami()
    df = df.drop("jdate").with_columns(symbol = pl.lit("EMAMI"))
    await insert_df(df)


@asset
async def update_ons():
    df = tgju_.ons()
    df = df.drop("jdate").with_columns(symbol = pl.lit("XAUUSD"))
    await insert_df(df)
