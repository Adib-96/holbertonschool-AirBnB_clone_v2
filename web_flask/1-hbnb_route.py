#!/usr/bin/python3

"""
Flask application
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display a message to the user"""
    return "Hello HBNB!"


@app.route('/hbnh', strict_slashes=False)
def hbnh():
    return "HBNB"


if __name__ == '__main__':
    """Run the main program"""
    app.run(host='0.0.0.0', port=5000)
