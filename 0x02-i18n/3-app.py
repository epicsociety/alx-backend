#!/usr/bin/env python3
""" instantiated the Babel object and configure it using the Config
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ instantiated the Babel object and configure it
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """ Render a simple page"""
    return render_template('3-index.html', title=_("home_title"),
                           header=_("home_header"))


@babel.localeselector
def get_locale():
    """ determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
