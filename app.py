from aiohttp import web
from api.auth.routes import routes as auth_routes


app = web.Application()


app.add_routes(auth_routes)


if __name__ == '__main__':
    web.run_app(app)
