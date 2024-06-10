from aiogram import Bot
from aiohttp import web

routes = web.RouteTableDef()


async def start_http(bot: Bot):
    @routes.get('/')
    async def hello(request):
        return web.Response(text="Hello, world")

    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)

