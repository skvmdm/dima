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
    status = '200 OK'
    start_response(status, response_headers)
    return [output]

def test(environ, start_response):
    request = json.loads(environ['wsgi.input'].read())

    response = {}
    response["version"] = request["version"]
    response["session"] = request["session"]
    response["response"] = {"end_session" : False}
    response["response"]["text"] = "Привет!"
    response["response"]["end_session"] = True
    output = json.dumps(response).encode('utf-8')

    response_headers = [('Content-type', 'text/plain'),
                  ('Content-Length', str(len(output)))]
    status = '200 OK'
    start_response(status, response_headers)
    return [output]



if __name__=="__main__":
    wsgi_handler = WSGIHandler(noop_application)
    test_wsgi_handler = WSGIHandler(test)
    app = web.Application()
    app.router.add_route("*", "/{path_info:noop.*}", wsgi_handler)
    app.router.add_route("*", "/{path_info:api/noop.*}", wsgi_handler)
    app.router.add_route("*", "/{path_info:test.*}", test_wsgi_handler)
    app.router.add_route("*", "/{path_info:api/test.*}", test_wsgi_handler)
    app.router.add_post("/noop", noop_application)
    app.router.add_post("/api/noop", noop_application)
    app.router.add_post("/test", test)
    app.router.add_post("/api/test", test)
    web.run_app(app)