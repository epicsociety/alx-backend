#!/usr/bin/env python3
""" instantiated the Babel object and configure it using the Config
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ tantiated the Babel object and configure it
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """ Render a simple page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
