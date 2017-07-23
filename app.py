from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "My first flask app"

app.run(port = 5000)
