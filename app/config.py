#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

class Config(object):
    SECRET_KET = "CHANGE_AS_YOU_WANT"
    BCRYPT_LOG_ROUNDS = 13
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DB_NAME = "dev.db"
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    ASSETS_DEBUG = True

class ProdConfig(Config):
    ENV = 'dev'
    DB_NAME = "prod.db"
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
