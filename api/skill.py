import aiohttp
from aiohttp import web

app = web.Application()

HOST_IP = "0.0.0.0"
HOST_PORT = 1254

async def skill_space(request_obj):
    request = await request_obj.json()

    response = {}
    response["version"] = request["version"]
    response["session"] = request["session"]
    response["response"] = {"end_session" : False}

    response["response"]["text"] = "Привет!"
    response["response"]["end_session"] = True

    return web.json_response(response)


def init():
    #app = web.Application()
    app.router.add_post("/skill_space", skill_space)
    web.run_app(app, host = HOST_IP, port = HOST_PORT)

if __name__=="__main__":
    init()
