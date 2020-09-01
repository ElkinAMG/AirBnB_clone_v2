#!/usr/bin/python3
"""
Write a script that starts a Flask web application.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Some comments explaining what this function does.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Some comments explaining what this function does.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cistext(text):
    """Some comments explaining what this function does.
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
