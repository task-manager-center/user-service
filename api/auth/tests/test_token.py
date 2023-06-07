from datetime import timedelta
from time import sleep

from api.auth.token import create_access_token, parse_token


def test_jwt_token():
	user_id = 1
	token = create_access_token(user_id=user_id, expires_delta=timedelta(seconds=5))
	assert token is not None

	user_id_from_token = parse_token(token=token)
	assert user_id_from_token == user_id

	sleep(5)
	user_id_from_token = parse_token(token=token)
	assert user_id_from_token is None


def test_validation_token():
	invalid_token = "token"
	assert parse_token(token=invalid_token) is None
