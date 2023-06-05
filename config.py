import os
from dotenv import load_dotenv


load_dotenv()


class DBConfig:
	DB_URI: str = os.environ.get("DB_URI", "postgresql+asyncpg://postgres:postgres@localhost:5432/user_service")


class PasswordConfig:
	SALT: str = os.environ.get("SALT")


class TokenConfig:
	SECRET_KEY: str = os.environ.get("SECRET_KEY", "secret")


class BaseConfig(
	DBConfig,
	PasswordConfig,
	TokenConfig,
):
	DEBUG: bool = os.environ.get("DEBUG", False)


config = BaseConfig()
