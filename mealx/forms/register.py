#!/usr/bin/env python

from flask_wtf import Form
from wtforms import TextField, PasswordField, validators

class RegisterForm(Form):
    username = TextField('username', [])
    password = PasswordField('password', [])
    password2 = PasswordField('password-again', [])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        return True
