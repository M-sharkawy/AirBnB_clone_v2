#!/usr/bin/python3
'''script that starts a Flask web application'''

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """returns C <text>"""
    text2 = text.replace("_", " ")
    return f"C {text2}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
