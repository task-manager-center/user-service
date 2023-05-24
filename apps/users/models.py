from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, func

from libs.pg import Base


class User(Base):
	__tablename__ = "users"

	id: int = Column(Integer, primary_key=True)
	email: str = Column(String, unique=True, nullable=False)
	hashed_password: str = Column(String, nullable=False)

	created_at: datetime = Column(DateTime, default=datetime.utcnow, server_default=func.current_timestamp())

	def __repr__(self):
		return f"User <{self.id}>"

