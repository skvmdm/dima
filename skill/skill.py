import aiohttp
from aiohttp import web

HOST_IP = "0.0.0.0"
HOST_POST = 1254

async def skill_space(request_obj):
    request = await request_obj.json()


def init():
    app = web.Application()
    app.router.add_post("/skill_space", skill_space)
    web.run_app(app, host = HOST_IP, port = HOST_PORT)

if __name__=="__main__":
    init()

