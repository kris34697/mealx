import os
import base64
import flask

from flask_login import LoginManager
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

def create_app():
    app = flask.Flask(__name__)
    return app

#TODO change this stuff to application factory

app = create_app()

app.config.from_object('config')
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

mongo = PyMongo(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)

from .models.user import User

class Unauthorized(Exception):
    """Unauthorized Access."""

@login_manager.user_loader
def load_user(user_id):
    return User.by_id(user_id) 

@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.args.get('api_key')
    if api_key:
        user = User.by_apikey(api_key)
        if user:
            return user
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        try:
            api_key = base64.b64decode(api_key).decode()
        except TypeError:
            pass
        user = User.by_apikey(api_key)
        if user:
            return user
    return None


@login_manager.unauthorized_handler
def unauthorized():
    raise Unauthorized()

from . import views
from .filters import filters

app.register_blueprint(filters)
app.register_blueprint(views.ui)
