#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(stuff):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    states = list(storage.all("State").values())
    states.sort(key=lambda i: i.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
