import os
import logging
import dotenv
from sqlmodel import create_engine

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_file = os.path.join(ROOT_DIR, ".env.config")


def config(engin: str, name: str, user: str, password: str, host: str, port: int):
    url: str = f"{engin.lower()}://{user}:{password}@{host}:{port}/{name}"
    dotenv.set_key(dotenv_file, key_to_set="DATABASES_URL", value_to_set=f"{url}")


def conn_uri():
    if os.path.isfile(dotenv_file):
        dotenv.load_dotenv(dotenv_file)
        return os.getenv("DATABASES_URL")
    logging.error("Pleas config your Database!")


def conn_engine():
    return create_engine(conn_uri(), echo=True)
