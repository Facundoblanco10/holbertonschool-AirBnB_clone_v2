#!/usr/bin/python3
""" script that starts a Flask web application"""

from flask import Flask
from flask import render_template
from flask import request
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_page():
    from models.state import State
    from models.amenity import Amenity
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities)


@app.teardown_appcontext
def remove(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
