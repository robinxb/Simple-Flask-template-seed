#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint("user", __name__, static_folder="static")

@blueprint.route("/", methods=["GET"])
def index():
    return render_template("index.html")
