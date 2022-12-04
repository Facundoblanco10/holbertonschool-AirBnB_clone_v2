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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_page(text="is cool"):
    return "Python " + str(text).replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number_page(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
