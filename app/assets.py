#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask.ext.assets import Bundle, Environment

js = Bundle('libs/jquery/dist/jquery.min.js')
css = Bundle('css/style.css')

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)
