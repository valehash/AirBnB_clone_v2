#!/usr/bin/python3
"""Python script to begin web apps"""

from flask import Flask, render_template

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
        Returns: HBNB
    """
    return "<p>HBNB</p>"


@app.route("/c/<subpath>", strict_slashes=False )


def display_user_path(subpath):
    """Function to display the user subpath
        Returns: c and a propt from the user
    """
    subpath =  subpath.replace('_', ' ')
    return f"C {subpath}"


@app.route("/python", strict_slashes=False)


@app.route("/python/<subpath>", strict_slashes=False)


def display_python(subpath="is cool"):
    """Function to display the user subpath
        Returns: python and the user prompt
    """
    subpath =  subpath.replace('_', ' ')
    return f"Python {subpath}"


@app.route("/number/<num>", strict_slashes=False)


def display_number(num):
    """Function to display the user subpath
        Returns: prompt is a number
    """
    if isinstance(num, int):
        return f"{num} is a number"
    else:
        app.aborter(404)



@app.route("/number_template/<int:num>", strict_slashes=False)
def template_number(num):
    """Function to display the user subpath
        Returns: prompt is a number
    """
    if not isinstance(num, int):
        return app.aborter(404)
    return render_template('5-number.html', number=num)


@app.route("/number_odd_or_even/<int:num>", strict_slashes=False)
def template_even_or_odd(num):
    """Function to display the user subpath
        Returns: prompt is a number
    """
    if not isinstance(num, int):
        return app.aborter(404)

    if num % 2 == 0:
        string = "is even"
    else:
        string = "is odd"
    return render_template('6-number_odd_or_even.html', number=num, text=string)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
