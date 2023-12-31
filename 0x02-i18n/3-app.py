#!/usr/bin/env python3
""" instantiated the Babel object and configure it using the Config
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ instantiate the Babel object and configure it
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index() -> str:
    """ Render a simple page"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> str:
    """ determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
