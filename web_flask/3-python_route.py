#!/usr/bin/python3
"""Python script to begin web apps"""

from flask import Flask

app =  Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/", strict_slashes=False)
def Hello_hbnb():
    """Function to display the HELLO HBNB in the root route
        Returns: a greeting
    """
    return "<p>Hello, HBNB!</p>"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """Function to display the HELLO HBNB in the /hbnb route
        Returns: a greeting
    """
    return "<p>HBNB</p>"

@app.route("/c/<subpath>", strict_slashes=False )
def display_user_path(subpath):
    """Function to display the user subpath
        Returns: a greeting
    """
    subpath =  subpath.replace('_', ' ')
    return f"C {subpath}"

@app.route("/python", strict_slashes=False)
@app.route("/python/<subpath>", strict_slashes=False)
def display_python(subpath="is cool"):
    """Function to display the user subpath
        Returns: a greeting
    """
    subpath =  subpath.replace('_', ' ')
    return f"Python {subpath}"








if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
