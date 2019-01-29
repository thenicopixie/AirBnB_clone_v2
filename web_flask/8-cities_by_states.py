#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(stuff):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_cities_list():
    states = list(storage.all("State").values())
    states.sort(key=lambda i: i.name)
    cities = list(storage.all("City").values())
    cities.sort(key=lambda i: i.name)
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
