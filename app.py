"""imports"""
import os
import json
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from db import mongoConnect

app = Flask(__name__)

load_dotenv()
print(os.getenv('CONNECTION_STRING'))


def add2(n):
    '''
    Add 2 to a number
    '''
    return n+2
 

 
@app.route("/items", methods=["GET"])
def get_data():
    """set every page with 100 items """
    page = int(request.args.get("page",0))
    per_page = 100
    page = 1
    data = list(mongoConnect.collection.find().skip((page - 1) * per_page).limit(per_page))
    print(page)
    return jsonify(json.loads( json.dumps(data,default=str)))


@app.route('/')
def index():
    '''
    Index page
    '''
    return jsonify(dict(name='John', age=25, city='New York'))

@app.route('/buy_or_sale')
def buy_or_sale():
    '''update all if buy or sale''' 

    # get all recordes from db;

    # loop over each

    # update if buy or sale in mongodb;
    '''
    {
"_id": "65d4fb09d44f42f5cd8610c4",
"category": "sale",
"created_at": "2023-09-12 10:50:56",
"massage_content": "Wts\nSamsung Arabic \n\nM54 8/256\nMoq\n\nReady Fze",
"massage_type": "text",
"phone_id_new": 663,
"type": "buy",
},

    '''


    ...

if __name__ == '__main__':
    app.run('127.0.0.1', port=8000,   )
