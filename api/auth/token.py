from datetime import timedelta, datetime
from typing import Optional

import jwt
from jwt import DecodeError

from config import config

ALGORITHM = "HS256"


def create_access_token(user_id: int, expires_delta: timedelta = None) -> str:
	if expires_delta:
		expire = datetime.utcnow() + expires_delta
	else:
		expire = datetime.utcnow() + timedelta(minutes=10)

	to_encode = {
		"exp": expire,
		"user_id": user_id,
	}
	return jwt.encode(to_encode, config.SECRET_KEY, algorithm=ALGORITHM)


def parse_token(token: str) -> Optional[int]:
	try:
		payload = jwt.decode(token, config.SECRET_KEY, algorithms=[ALGORITHM])
	except DecodeError:
		return

	expire = payload.get("expire")
	if not expire or expire < datetime.utcnow():
		return

	return payload.get("user_id")
