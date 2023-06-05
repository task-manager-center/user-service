from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, func, select
from sqlalchemy.exc import IntegrityError

from apps.users import exc
from apps.users.hashing import password_hashing
from libs.pg import Base, ainsert, async_session


class User(Base):
	__tablename__ = "users"

	id: int = Column(Integer, primary_key=True)
	email: str = Column(String, unique=True, nullable=False)
	hashed_password: str = Column(String, nullable=False)

	created_at: datetime = Column(DateTime, default=datetime.utcnow, server_default=func.current_timestamp())

	def __repr__(self):
		return f"User <{self.id}>"

	@staticmethod
	async def create_user(email: str, password: str) -> "User.id":
		try:
			return await ainsert(
				model=User,
				data={
					"email": email,
					"hashed_password": password_hashing.hash_password(password=password)
				},
				returning=User.id,
			)
		except IntegrityError:
			raise exc.UserAlreadyExistException

	@staticmethod
	async def get_user(email: str, password: str) -> "User":
		async with async_session() as session:
			result = await session.execute(select(User).where(User.email == email).limit(1))

		user = result.scalars().first()
		if not user:
			raise exc.UserDoesNotExistException

		if not password_hashing.check_password(password=password, hashed_password=user.hashed_password):
			raise exc.UserDoesNotExistException

		return user
