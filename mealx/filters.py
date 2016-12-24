#!/usr/bin/env python

import jinja2
from flask import Blueprint

import datetime
import babel
import locale

filters = Blueprint('filters', __name__)

@jinja2.contextfilter
@filters.app_template_filter()
def do_datetime(context, value):
    return babel.dates.format_datetime(
        value, "yyyy-MM-dd"
    )
