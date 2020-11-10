# -*- coding: utf-8 -*-

from flask import Flask
from config import config
from .api import configure_api
from flask_cors import CORS


def create_app(config_name):
    app = Flask('aceSolarPower')
    CORS(app)
    app.config.from_object(config[config_name])
    configure_api(app)
    return app

