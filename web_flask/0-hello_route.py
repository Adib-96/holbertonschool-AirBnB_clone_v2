#!/usr/bin/python3

"""
Flask application
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Display a message to the user"""
    return "<p>Hello HBNB!</p>"


if __name__ == '__main__':
    """Run the main program"""
    app.run()
