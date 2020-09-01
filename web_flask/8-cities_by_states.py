#!/usr/bin/python3
"""Write a script that starts a Flask web application.
"""
from flask import flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def state_list():
    """Displays a HTML with a list of states.
    """
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db():
    """Close connection with DB.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')