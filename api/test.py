import aiohttp
import json
from aiohttp import web
from aiohttp_wsgi import WSGIHandler

HOST_IP = "0.0.0.0"
HOST_PORT = 1254

def noop_application(environ, start_response):
    request_body = environ['wsgi.input'].read() # returns bytes object
    request = json.loads(request_body)
    
    readstr = request_body.decode('utf-8') 
    status = '200 OK'
    #output = b'Hello World!\n'

    response = {}
    response["version"] = request["version"]
    response["session"] = request["session"]
    response["response"] = {"end_session" : False}
    response["response"]["text"] = "Привет!"
    response["response"]["end_session"] = True

    output = json.dumps(response).encode('utf-8')

    response_headers = [('Content-type', 'text/plain'),
                  ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]

async def test(request_obj):
    request = await request_obj.json()

    response = {}
    response["version"] = request["version"]
    response["session"] = request["session"]
    response["response"] = {"end_session" : False}
    response["response"]["text"] = "Привет!"
    response["response"]["end_session"] = True

    return web.json_response(response)

wsgi_handler = WSGIHandler(noop_application)
test_wsgi_handler = WSGIHandler(test)
app = web.Application()

if __name__=="__main__":
    app.router.add_route("*", "/{path_info:hello.*}", wsgi_handler)
    app.router.add_route("*", "/{path_info:test.*}", test_wsgi_handler)
    app.router.add_post("/hello", wsgi_handler)
    app.router.add_post("/apihello", wsgi_handler)
    app.router.add_post("/test", test_wsgi_handler)
    app.router.add_post("/api/test", test_wsgi_handler)
    web.run_app(app)