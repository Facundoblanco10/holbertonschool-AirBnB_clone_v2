#!/usr/bin/python3
""" script that starts a Flask web application"""

from flask import Flask
from flask import render_template
from flask import request
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id_page(id=None):
    from models.state import State
    states = storage.all(State).values()
    state = None
    for i in states:
        if id == i.id:
            state = i
            break
    return render_template('9-states.html', states=states, 
                                            state=state,
                                            id=id)

@app.teardown_appcontext
def remove(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
