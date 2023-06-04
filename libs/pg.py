from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from config import config


async_engine = create_async_engine(config.DB_URI, echo=True)
Base = declarative_base()
async_session = async_sessionmaker(async_engine, expire_on_commit=False)
