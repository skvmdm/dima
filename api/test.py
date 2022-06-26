from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page Route - nice work Andrew!!!'


@app.route('/test')
def about():
    return 'test Page Route'

