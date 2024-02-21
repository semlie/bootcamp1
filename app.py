from service.dataManipulation import clean_smartphone_list
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def products():
    data = clean_smartphone_list()
    return data

if __name__ == '__main__':
    app.run('127.0.0.1', port=8001, debug=True)
