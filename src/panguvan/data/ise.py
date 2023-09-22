import datetime
from typing import Optional, List, Tuple
from oxtapus.ise import TSETMC
import polars as pl
import pandas as pd
from ..engin import conn_engine, conn_uri
from ..utils import get_last_market_activity_datetime, df_date


class ISE:
    def __init__(
        self,
        daily_hist_price: bool = True,
        daily_adj_hist_price: bool = True,
        intraday_trades: bool = True,
    ):
        self.daily_hist_price = daily_hist_price
        self.daily_adj_hist_price = daily_adj_hist_price
        self.intraday_trades = intraday_trades
        self.tsetmc = TSETMC()
        self.engine = conn_engine()
        self.conn_uri = conn_uri()
        self.last_market_activity_datetime: Optional[datetime.date] = None
        self.last_update_date: Optional[datetime.date] = None
        self.last_call_update_date: Optional[datetime.date] = None

    def write_date_table(self):
        df = df_date()
        df.write_database(
            table_name="date", if_exists="append", connection_uri=self.conn_uri
        )

    def write_trbc_tables(self, trbc_hdf_path):
        """Append The Refinitiv Business Classification data to tables"""
        items = [
            "economic_sector",
            "business_sector",
            "industry_group",
            "industry",
            "activity",
        ]
        for i in items:
            df = pl.from_pandas(pd.read_hdf(trbc_hdf_path, key=i))
            df.write_database(
                table_name=f"ise_{i}", if_exists="append", connection_uri=self.conn_uri
            )

    def write_market_table(
        self, id: List[int] = [1, 2, 3], name: List[str] = ["tse", "ifb", "ifb-otc"]
    ):
        df = pl.DataFrame(
            {
                "id": id,
                "name": name,
            }
        )
        df.write_database(
            table_name="ise_market", if_exists="append", connection_uri=self.conn_uri
        )

    def get_last_update_date(self, table):
        query = f"SELECT date FROM {table}"
        max_date = (
            pl.read_database(query=query, connection_uri=self.conn_uri)
            .max()
            .drop_nulls()
        )
        if max_date.is_empty():
            return False
        return max_date.row(0, named=True)["date"]

    def handle_update_date(self, table):
        if not self.last_market_activity_datetime:
            self.last_market_activity_datetime = get_last_market_activity_datetime()
        if not self.last_update_date:
            self.last_update_date = self.get_last_update_date(table)
        if (not self.last_update_date) or (
            self.last_update_date < self.last_market_activity_datetime.date()
        ):
            return False
        return True

    def update_daily_hist_price(self, instruments: List[Tuple[str, int]]):
        """Get hist-price and push on table.
        :param instruments: List[Tuple[str, int]], [(ins_id, ins_code), ...]
        :return:
        """
        cols = [
            "ins_id",
            "date",
            "open",
            "low",
            "high",
            "close",
            "final",
            "y_final",
            "volume",
            "value",
        ]
        table = "ise_daily_hist_price"
        error_log_ins = []
        if not self.handle_update_date(table):
            for ins in instruments:
                df = self.tsetmc.hist_price(ins_code=ins[1])
                df["ins_id"] = ins[0]
                df = pl.from_pandas(df.reset_index()[cols])
                df.write_database(
                    table_name=table, if_exists="append", connection_uri=self.conn_uri
                )

    def update_daily_adj_hist_price(self):
        pass
