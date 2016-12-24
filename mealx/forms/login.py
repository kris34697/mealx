#!/usr/bin/env python

from flask_wtf import Form
from wtforms import TextField, PasswordField, validators

class LoginForm(Form):
    username = TextField('username', [])
    password = PasswordField('password', [])

#   def __init__(self, *args, **kwargs):
#        Form.__init__(self, *args, **kwargs)
#        self.user = None
#
#    def validate(self):
#        rv = Form.validate(self)
#        if not rv:
#            return False
#
#        user = User.by_name(self.username.data)
#
#        if user is None:
#            self.username.errors.append('Unknown username')
#            return False
#
#        if not user.check_password(self.password.data):
#            self.password.errors.append('Invalid password')
#            return False
#
#        self.user = user
#        return True
