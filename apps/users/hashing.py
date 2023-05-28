import hashlib

from config import config


class PasswordHash:
	salt = config.SALT

	def hash_password(self, password: str) -> str:
		password = (password + self.salt).encode("utf-8")
		return hashlib.sha256(password).hexdigest()

	def check_password(self, password: str, hashed_password: str) -> bool:
		password_to_check = self.hash_password(password=password)
		return hashed_password == password_to_check


password_hashing = PasswordHash()
