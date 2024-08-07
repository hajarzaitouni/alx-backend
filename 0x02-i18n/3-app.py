#!/usr/bin/env python3
""" Parametrize templates """

from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import Union

app = Flask(__name__)
babel = Babel(app)


class Config():
    """ create Config class for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """ Determine the best match for supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """ return hello world template. """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
