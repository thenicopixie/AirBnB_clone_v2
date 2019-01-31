#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(stuff):
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def filters():
    states = list(storage.all("State").values())
    states.sort(key=lambda i: i.name)
    cities = list(storage.all("City").values())
    amenities = list(storage.all("Amenity").values())
    places = list(storage.all("Place").values())
    cities.sort(key=lambda i: i.name)
    amenities.sort(key=lambda i: i.name)
    places.sort(key=lambda i: i.name)
    return render_template('100-hbnb.html', states=states,
                           cities=cities, amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
