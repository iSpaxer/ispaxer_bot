import asyncio
import json

from aiohttp import web


async def handle(request):
    return web.Response(text=json.dumps("Hello!"))


async def main():
    app = web.Application()
    app.add_routes([web.get('/', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8056)
    await site.start()

    while True:
        await asyncio.sleep(3600)


if __name__ == '__main__':
    asyncio.run(main())
