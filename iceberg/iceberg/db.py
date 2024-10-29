import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker

load_dotenv()
LODAD_DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = LODAD_DATABASE_URL if LODAD_DATABASE_URL else ""


# Create the async engine
async_engine = create_async_engine(DATABASE_URL, echo=True)
# Create an async sessionmaker
async_session = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)
