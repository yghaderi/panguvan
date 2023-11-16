import os
import logging
from typing import List
import dotenv
from sqlmodel import create_engine
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


async def write_df_to_db(table: str, df: pl.DataFrame):
    conn = await asyncpg.connect(database_url())
    result = await conn.copy_records_to_table(table, records=df.to_numpy(), columns=df.columns)
    logging.info(result)
    await conn.close()


async def write_records_to_db(table: str, records: List[list[any]], columns: List[str]):
    conn = await asyncpg.connect(database_url())
    result = await conn.copy_records_to_table(table, records=records, columns=columns)
    logging.info(result)
    await conn.close()
