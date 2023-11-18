import os
import logging
from datetime import datetime
from typing import List
import dotenv
import asyncpg
import polars as pl

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_file = os.path.join(ROOT_DIR, ".env.config")


def config(engin: str, name: str, user: str, password: str, host: str, port: int):
    url: str = f"{engin.lower()}://{user}:{password}@{host}:{port}/{name}"
    dotenv.set_key(dotenv_file, key_to_set="DATABASES_URL", value_to_set=f"{url}")


def database_url():
    if os.path.isfile(dotenv_file):
        dotenv.load_dotenv(dotenv_file)
        return os.getenv("DATABASES_URL")
    logging.error("Pleas config your Database!")


async def write_df(table: str, df: pl.DataFrame) -> None:
    """
    Parameters
    ---------
    table: str
        table name
    df : polars.DataFrame
        data-frame
    """
    conn = await asyncpg.connect(database_url())
    result = await conn.copy_records_to_table(
        table, records=df.to_numpy(), columns=df.columns
    )
    print(
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {result} to {table!r} table."
    )
    await conn.close()


async def write_records(
    table: str, records: List[list[any]], columns: List[str]
) -> None:
    """
    Parameters
    ---------
    table: str
        table name
    records : List[list[any]]
        records
    columns: List[str]
        columns name
    """
    conn = await asyncpg.connect(database_url())
    result = await conn.copy_records_to_table(table, records=records, columns=columns)
    print(
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {result} records to {table!r} table."
    )
    await conn.close()


async def fetch(query: str) -> List[any]:
    """
    Parameters
    ---------
    query: str
        Query arguments.

    Returns
    -------
    A list of Record instances.
    """
    conn = await asyncpg.connect(database_url())
    result = await conn.fetch(query)
    await conn.close()
    return result
