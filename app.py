
from os import name
import os
from flask import Flask, jsonify
app = Flask(__name__)
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('CONNECTION_STRING'))


def add2(n):
    return n+2

@app.route('/')
def index():

    return jsonify(dict(name='John', age=25, city='New York'))


if __name__ == '__main__':
    app.run('127.0.0.1', port=8000,  debug=True)
