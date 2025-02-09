#!/usr/bin/python3
'''script that starts a Flask web application'''

from flask import Flask, render_template

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


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """returns python <text>"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """returns n is a number"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_t(n):
    """returns n is a number"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """returns n is odd or even"""
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", n=n, odd_even="even")
    else:
        return render_template("6-number_odd_or_even.html", n=n, odd_even="odd")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
