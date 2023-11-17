import asyncio
import datetime
from typing import Optional, List, Tuple
import polars as pl
import pandas as pd
from oxtapus import TSETMC
from panguvan.db import write_df_to_db, write_records_to_db, fetch

loop = asyncio.get_event_loop()


def write_trbc_tables(trbc_hdf_path: str) -> None:
    """
    .. raw:: html

        <div dir="rtl">
            داده‌هایِ efinitiv Business Classification رو در جدول‌هایِ مربوطه کپی می‌کنه.
        </div>

    Parameters
    ---------
    trbc_hdf_path: str
        TRBC.h5 . You can download this file `here`_.
        .. _here: https://github.com/yghaderi/panguvan/blob/master/TRBC.h5
    """
    items = [
        "economic_sector",
        "business_sector",
        "industry_group",
        "industry",
        "activity",
    ]
    for i in items:
        df = pl.from_pandas(pd.read_hdf(trbc_hdf_path, key=i))
        loop.run_until_complete(write_df_to_db(table=f"tsetmc_{i}", df=df))
        loop.close()


def write_market_table(
        id: Tuple[int] = (1, 2, 3), name: Tuple[str] = ("tse", "ifb", "ifb-otc")
) -> None:
    """
    .. raw:: html

        <div dir="rtl">
            اسمِ بازارهایِ بورسِ ایران رو در جدولِ بازار می‌ریزه.
        </div>

    Parameters
    ----------
    id: Tuple[int] , default (1, 2, 3)
        اندیسِ بازار
    name: Tuple[str] , default ("tse", "ifb", "ifb-otc")
        نامِ بازار
    """
    df = pl.DataFrame(
        {
            "id": id,
            "name": name,
        }
    )
    loop.run_until_complete(write_df_to_db(table=f"tsetmc_market", df=df))
    loop.close()


def _get_max_date(table: str):
    query = f"SELECT  MAX(date) as max FROM {table}"
    result = loop.run_until_complete(fetch(query))
    loop.close()
    return result[0]["max"]


def _get_stock():
    query = f"SELECT ins_id, ind_code FROM tsetmc_stock"
    result = loop.run_until_complete(fetch(query))
    loop.close()
    return result


def _handle_update_date(table: str):
    last_update_date = _get_max_date(table)
    if last_update_date:
        if last_update_date < TSETMC().last_market_activity_datetime().date():
            return last_update_date
    return False


def update_daily_hist_price():
    """
    Get hist-price and push on table.
    """
    tsetmc = TSETMC()
    cols = [
        "date",
        "ins_id",
        "open",
        "high",
        "low",
        "close",
        "final",
        "y_final",
        "volume",
        "value",
        "trade_count"
    ]
    table = "tsetmc_stock_daily_hist_price"
    date = _handle_update_date(table)
    stocks_list = _get_stock()
    if not date:
        for stock in stocks_list:
            df = tsetmc.hist_price(ins_code=stock["ins_code"])
            df = df.with_columns(pl.lit(stock["ins_id"]).alias("ins_id")).select(cols)
            loop.run_until_complete(write_df_to_db(table=table, df=df))
            loop.close()
    else:
        for stock in stocks_list:
            df = tsetmc.hist_price(ins_code=stock["ins_code"])
            df = df.with_columns(pl.lit(stock["ins_id"]).alias("ins_id")).select(cols).filter(pl.col("date") > date)
            loop.run_until_complete(write_df_to_db(table=table, df=df))
            loop.close()
