'''
 This is a simple Flask app that returns a JSON object. The app is running on port 8000.
'''
from flask import Flask, jsonify
import buying_or_selling as bos
app = Flask(__name__)


def add2(n):
    '''
    Add 2 to a number
    '''
    return n+2


@app.route('/')
def index():
    '''
    Index page
    '''
    return jsonify(dict(name='John', age=25, city='New York'))


@app.route('/buy_or_sale')
def buy_or_sale():
    '''Update MongoDB documents based on inferred intents.'''
    data =  bos.collection.find()  # Assuming JSON data is sent in the request
    for item in data:
        content = item["massage_content"]
        inferred_intent = bos.check_intent(content)
        bos.update_mongo(item["_id"], inferred_intent)
    return jsonify({"message": "Updated successfully"})


if __name__ == '__main__':
    app.run('127.0.0.1', port=8000,  debug=True)
