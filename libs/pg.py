from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from config import config


engine = create_engine(config.DB_URI)
Base = declarative_base()
async_session = async_sessionmaker(create_async_engine(config.DB_URI, echo=True), expire_on_commit=False)

