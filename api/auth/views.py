from aiohttp.web import Request, HTTPUnprocessableEntity
from aiohttp.web_exceptions import HTTPConflict

from apps.users import exc
from apps.users.models import User


async def signup(request: Request):
	data = await request.json()
	try:
		email = data["email"]
		password = data["password"]

		user_id = await User.create_user(email=email, password=password)
	except KeyError:
		raise HTTPUnprocessableEntity(body="User with given email already exist")
	except exc.UserAlreadyExistException:
		raise HTTPConflict(body="User with given email already exist")

	



async def login(request):
	...


async def refresh_token(request):
	...
