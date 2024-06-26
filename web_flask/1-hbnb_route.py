#!/usr/bin/python3
"""Python script to begin web apps"""

from flask import Flask

app =  Flask(__name__)

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
