from flask import Flask, jsonify
from test import *

app = Flask(__name__)

print (true("kk"))

# Data to be served by the API
employees = [
    {'id': 1, 'name': 'Ashley'},
    {'id': 2, 'name': 'Kate'},
    {'id': 3, 'name': 'Joe'},
    {'id': 4, 'name': 'James'}
]

#print(employees["name"])

# Basic dictionary example
#d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}


print("hi schooner tuna")

@app.route("/")
def hello_world():
    return "<p>Hello Bob, Schooner Tuna World!</p>" + true("kk")

# Define a route for the API
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

if __name__ == '__main__':
    app.run(debug=True)

    # to run:
    #python -m flask --debug run