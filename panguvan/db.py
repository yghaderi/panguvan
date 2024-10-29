import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema

load_dotenv()
LODAD_DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = LODAD_DATABASE_URL if LODAD_DATABASE_URL else ""


engine = create_engine(DATABASE_URL)
with engine.connect() as connection:
    connection.execute(CreateSchema("tgju", if_not_exists=True))
    connection.commit()
