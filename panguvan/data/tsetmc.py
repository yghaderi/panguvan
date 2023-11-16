import datetime
from typing import Optional, List, Tuple
from oxtapus.ise import TSETMC
import polars as pl
import pandas as pd


from panguvan.db import conn_engine, conn_uri
from panguvan.utils import df_date


class ISE:
    """
    Get **Iran Stock Exchange** data and update them by https://github.com/yghaderi/oxtapus.
    """

    def __init__(
        self,
    ):
        self.tsetmc = TSETMC()
        self.engine = conn_engine()
        self.conn_uri = conn_uri()
        self.last_market_activity_datetime: Optional[datetime.date] = None
        self.last_update_date: Optional[datetime.date] = None
        self.last_call_update_date: Optional[datetime.date] = None

    def write_date_table(self):
        """"""
        df = df_date()
        df.write_database(
            table_name="date", if_exists="append", connection_uri=self.conn_uri
        )

    def write_trbc_tables(self, trbc_hdf_path: str) -> None:
        """Append The Refinitiv Business Classification data to tables.
        Parameters
        ---------
        trbc_hdf_path: str
            TRBC.h5 file path. You can download this file `here`_.
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

    def _get_last_update_date(self, table):
        query = f"SELECT date FROM {table}"
        max_date = (
            pl.read_database(query=query, connection_uri=self.conn_uri)
            .max()
            .drop_nulls()
        )
        if max_date.is_empty():
            return False
        return max_date.row(0, named=True)["date"]

    def _handle_update_date(self, table):
        if not self.last_market_activity_datetime:
            self.last_market_activity_datetime = (
                self.tsetmc.get_last_market_activity_datetime()
            )
        if not self.last_update_date:
            self.last_update_date = self._get_last_update_date(table)
        if (not self.last_update_date) or (
            self.last_update_date < self.last_market_activity_datetime.date()
        ):
            return False
        return True

    def update_daily_hist_price(self, instruments: List[Tuple[str, int]]):
        """
        Get hist-price and push on table.
        Parameters
        ----------
        instruments: List[Tuple[str, int]], [(ins_id, ins_code), ...]
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
        if not self._handle_update_date(table):
            for ins in instruments:
                df = self.tsetmc.hist_price(ins_code=str(ins[1]))
                df["ins_id"] = ins[0]
                df = pl.from_pandas(df.reset_index()[cols])
                df.write_database(
                    table_name=table, if_exists="append", connection_uri=self.conn_uri
                )
        else:
            for ins in instruments:
                df = self.tsetmc.hist_price(ins_code=str(ins[1]))
                df["ins_id"] = ins[0]
                df = pl.from_pandas(df.reset_index()[cols])
                df.write_database(
                    table_name=table, if_exists="append", connection_uri=self.conn_uri
                )

    def update_daily_adj_hist_price(self):
        pass
