"""imports"""
import os
import json
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from db import mongoConnect

app = Flask(__name__)

load_dotenv()
print(os.getenv('CONNECTION_STRING'))

@app.route("/items", methods=["GET"])
def get_data():
    """set every page with 100 items """
    page = int(request.args.get("page",0))
    per_page = 100
    if not page:
        per_page = 0
        page = 0
    data = list(mongoConnect.collection.find().skip((page - 1) * per_page).limit(per_page))
    print(page)
    return jsonify(json.loads( json.dumps(data,default=str)))


@app.route('/')
def index():
    '''
    Index page
    '''
    return jsonify(dict(name='John', age=25, city='New York'))


if __name__ == '__main__':
    app.run('127.0.0.1', port=8000,   )
