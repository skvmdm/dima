from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/flask_app', methods = ['POST'])
def update_text():
    content = request.json
    status = '200 OK'
    #output = b'Hello World!\n'

    response = {}
    response["version"] = content["version"]
    response["session"] = content["session"]
    response["response"] = {"end_session" : False}
    response["response"]["text"] = "Привет!"
    response["response"]["end_session"] = True
    return response
