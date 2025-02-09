#

from flask import flask

app = flask(__name__)

@app.route("/", strict_slashes=False)
def root():
        return "Hello HBNB!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
