import os
from dotenv import load_dotenv


load_dotenv()


class DBConfig:
	DB_URI: str = os.environ.get("DB_URI", "postgresql+asyncpg://postgres:postgres@localhost:5432/user_service")


class PasswordConfig:
	SALT: str = os.environ.get("SALT")


class BaseConfig(
	DBConfig,
	PasswordConfig,
):
	DEBUG: bool = os.environ.get("DEBUG", False)


config = BaseConfig()
