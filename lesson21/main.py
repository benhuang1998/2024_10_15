from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, ben你好!</h1>"

@app.route('/hello')
def hello():
    return 'Hello, World'