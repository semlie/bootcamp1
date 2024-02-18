from os import name
from service.dataManipulation import extract_data

from flask import Flask
app = Flask(__name__)


@app.route('/')
def products():

    return extract_data()

if __name__ == '__main__':
    app.run('127.0.0.1', port=8000,  debug=True)
