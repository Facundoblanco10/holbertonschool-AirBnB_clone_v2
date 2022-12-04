#!/usr/bin/python3
""" script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def homepage():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_page(text=None):
    return "C " + str(text).replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
