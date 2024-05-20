#!/usr/bin/python3
"""Python script to begin web apps"""

from flask import Flask

app =  Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/", strict_slashes=False)
def Hello_hbnb():
    return "<p>Hello, HBNB!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
