class UserAlreadyExistException(Exception):
	"""Raise if user with given email already exist"""


class UserDoesNotExistException(Exception):
	"""Raise if user with given email does not exist or password doesn't match"""
