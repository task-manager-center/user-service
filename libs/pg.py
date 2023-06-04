from typing import List, Any

from sqlalchemy import Result, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from config import config


async_engine = create_async_engine(config.DB_URI, echo=True)
Base = declarative_base()
async_session = async_sessionmaker(async_engine, expire_on_commit=False)


async def ainsert(model: Base, data: List[dict]):
	"""
	Asynchronous insert into database
	:param model: database model
	:param data: [
		{"email": "email1", "hashed_password": "2134"},
		{"email": "email2", "hashed_password": "2134"},
	]
	:return: None
	"""
	async with async_session() as session:
		async with session.begin():
			await session.execute(
				insert(model),
				data,
			)
