import asyncio
from typing import Tuple
import polars as pl
import pandas as pd
from oxtapus import TSETMC
from panguvan.db import write_df, fetch

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
        loop.run_until_complete(write_df(table=f"tsetmc_{i}", df=df))
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
    loop.run_until_complete(write_df(table=f"tsetmc_market", df=df))
    loop.close()


def _get_max_date(table: str):
    query = f"SELECT  MAX(date) as max FROM {table}"
    result = loop.run_until_complete(fetch(query))
    loop.close()
    return result[0]["max"]


def _get_stocks():
    query = f"SELECT ins_id, ind_code FROM tsetmc_stock"
    result = loop.run_until_complete(fetch(query))
    loop.close()
    return result


def _handle_update_date(table: str):
    last_update_date = _get_max_date(table)
    if last_update_date:
        if last_update_date < TSETMC().last_market_activity_datetime().date():
            return True
    return False


class UpdateISE:
    def __init__(self):
        self.tsetmc = TSETMC()

    def stock_daily_hist_trade(self):
        """
        .. raw:: html

            <div dir="rtl">
                داده‌هایِ معالمه‌یِ سهام رو از ابتدا تا امروز یا روزي آخر رو با اختاپوس می‌گیره و در پایگاه-داده می‌ریزه.
            </div>
        """
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
            "trade_count",
        ]
        table = "ise_stock_daily_hist_trade"
        check_update_date = _handle_update_date(table)
        date = self.tsetmc.last_market_activity_datetime()
        stocks_list = _get_stocks()
        ins_id_list = [i["ins_id"] for i in stocks_list]
        if not check_update_date:
            for stock in stocks_list:
                df = self.tsetmc.hist_price(ins_code=stock["ins_code"])
                df = (
                    df.with_columns(pl.lit(stock["ins_id"]).alias("ins_id"))
                    .filter(pl.col("volume") > 0)
                    .select(cols)
                )
                loop.run_until_complete(write_df(table=table, df=df))
                loop.close()
        elif check_update_date:
            df = self.tsetmc.mw("stock").filter(
                (pl.col("ob_level") == 1)
                & (pl.col("volume") > 0)
                & (pl.col("ins_id").is_in(ins_id_list))
            )
            df = df.with_columns(pl.lit(date).alias("date")).select(cols)
            loop.run_until_complete(write_df(table=table, df=df))
            loop.close()

    def specific_option_data(self):
        """
        .. raw:: html

            <div dir="rtl">
                داده‌هایِ معالمه‌یِ سهام رو از ابتدا تا امروز یا روزي آخر رو با اختاپوس می‌گیره و در پایگاه-داده می‌ریزه.
            </div>
        """
        table = "ise_option_daily_hist_trade"
        omw_cols = [
            "ins_id",
            "open",
            "high",
            "low",
            "close",
            "final",
            "volume",
            "value",
            "trade_count",
        ]
        sod_cols = ["ins_id", "open_interest", "k", "lot_size"]
        omw = (
            self.tsetmc.options_mw()
            .filter((pl.col("ob_level") == 1) & (pl.col("volume") >= 0))
            .select(omw_cols)
        )
        specific_option_data = self.tsetmc.specific_option_data(
            ins_id=omw["ins_id"].to_list()
        ).select(sod_cols)
        df = omw.join(specific_option_data, on="ins_id", how="inner")
        loop.run_until_complete(write_df(table=table, df=df))
        loop.close()
