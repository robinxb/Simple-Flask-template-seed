#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

from .config import DevConfig
from .extentions import (db, bcrypt, login_manager)
from .assets import assets
import views

def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    assets.init_app(app)
    login_manager.init_app(app)
    return None

def register_blueprints(app):
    app.register_blueprint(views.blueprint)
    return None
