from flask import Flask
from test import *

app = Flask(__name__)

print (true("kk"))

print("hi schooner tuna")

@app.route("/")
def hello_world():
    return "<p>Hello Bob, Schooner Tuna World!</p>"