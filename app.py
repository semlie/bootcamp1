'''
 This is a simple Flask app that returns a JSON object. The app is running on port 8000.
'''
from flask import Flask, jsonify
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


if __name__ == '__main__':
    app.run('127.0.0.1', port=8000,  debug=True)
