#!/usr/bin/python3
""" script that starts a Flask web application"""

from flask import Flask
from flask import render_template
from flask import request
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def name_id_page():
    from models.state import State
    print("before")
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def remove(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
