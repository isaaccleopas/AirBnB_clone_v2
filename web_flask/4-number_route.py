#!/usr/bin/python3
"""Starts Flask web app

The app listens on 0.0.0.0, port 5000
Route:
    /: Display "Hello HBNB!"
    /hbnb: Display "HBNB"
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): display 'Python ', followed by the value of the text
    /number/<n>: Display 'n is a number' only if n is an integer
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Displays 'Python' followed by the value of <text>.
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
