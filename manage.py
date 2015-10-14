#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask_script import Manager, Shell, Server
from flask_script.commands import Clean, ShowUrls

from app.app import create_app, db

from app.config import DevConfig

def _make_context():
    """Return context dict for a shell session so you can access
    app, db, and the User model by default.
    """
    return {'app': app, 'db': db}

app = create_app(DevConfig)
manager = Manager(app)

@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()

manager.add_command('server', Server())
manager.add_command("clean", Clean())
manager.add_command("shell", Shell(make_context=_make_context))

if __name__ == '__main__':
    manager.run()
