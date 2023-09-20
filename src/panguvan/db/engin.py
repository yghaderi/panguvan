from os import getenv, path
import logging
import dotenv
from sqlmodel import create_engine

dotenv_file = "./.env.config"


def config(engin: str, name: str, user: str, password: str, host: str, port: int):
    url: str = f"{engin.lower()}://{user}:{password}@{host}:{port}/{name}"
    dotenv.set_key(dotenv_file, key_to_set="DATABASES", value_to_set=f"{url}")


def conn_engine():
    if path.isfile(dotenv_file):
        dotenv.load_dotenv(dotenv_file)
        return create_engine(getenv("DATABASES"))
    logging.error("Pleas config your Database!")
