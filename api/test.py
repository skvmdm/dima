import aiohttp
from aiohttp import web

async def test(request):
    return web.json_response("Hello!")

app = web.Application()
app.router.add_post("/test", test)

if __name__ == '__main__':
    web.run_app(app)
