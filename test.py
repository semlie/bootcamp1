from flask import Flask
from testing.fiterData import hello

app = Flask(__name__)

@app.route('/')
def runingInit():
        return hello()

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000,  debug=True)
