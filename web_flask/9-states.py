#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(stuff):
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    states = list(storage.all("State").values())
    states.sort(key=lambda i: i.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    states = list(storage.all("State").values())
    cities = list(storage.all("City").values())
    states.sort(key=lambda i: i.name)
    cities.sort(key=lambda i: i.name)
    return render_template('9-states.html',
                           states=states, cities=cities, id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
