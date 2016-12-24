#!/usr/bin/env python

import datetime
import base64
import uuid
import sys

from flask_login import UserMixin
from bson.objectid import ObjectId

from .. import bcrypt, mongo

class User(UserMixin):
    def __init__(self, _id, username, password):
        self.id = _id
        self.password = password
        self.username = username

#   @staticmethod
#    def by_id(id):
#        try:
#            user = manage.users.find_user({'_id': ObjectId(id)})
#        except manage.users.UserNotFoundError:
#            return None
#        except:
#            return None
#        else:
#            return User(user.id, user.username, user.password)
#
#    @staticmethod
#    def by_name(name):
#        try:
#            user = manage.users.find_user({'username': name})
#        except manage.users.UserNotFoundError:
#            return None
#        else:
#            return User(user.id, user.username, user.password)
#
#    @staticmethod
#    def by_apikey(apikey):
#        username, password = apikey.split(':')
#        user = User.by_name(username)
#        if user and user.check_password(password):
#            return user
#        return None
#
#    def check_password(self, password):
#        return bcrypt.check_password_hash(self.password, password)
#
#    def is_authenticated(self):
#        return True
#
#    def is_active(self):
#        return True
#
#    def is_anonymous(self):
#        return False
#
#    def get_id(self):
#        return self.id
