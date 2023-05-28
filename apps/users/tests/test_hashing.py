from apps.users.hashing import password_hashing


def test_hash_password():
	password = "my-password"
	hashed_password = password_hashing.hash_password(password=password)

	assert hashed_password is not None

	assert password_hashing.check_password(password=password, hashed_password=hashed_password)
