from aiohttp import web

from api.auth.views import signup, login, refresh_token


routes = [
	web.post('/api/v1/signup/', signup),
	web.post('/api/v1/login/', login),
	web.post('/api/v1/refresh/', refresh_token),
]
