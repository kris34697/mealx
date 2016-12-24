from flask import (
    request, render_template, redirect, session, flash,
    url_for, jsonify, send_from_directory, send_file, g,
    Blueprint
)
from flask_login import login_required, login_user, logout_user, current_user


from ..models.user import User
from ..forms import LoginForm, RegisterForm
from .. import Unauthorized, bcrypt, forms

ui = Blueprint('ui', __name__)

@ui.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@ui.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@ui.errorhandler(Unauthorized)
def unauthorized(error):
    return redirect(url_for('.login'))

@ui.route('/')
#@login_required
def home():
    return render_template('home.html')

@ui.route('/meals')
def meals():
    return render_template('meals.html')

@ui.route('/meals/create')
def create_meal():
    return render_template('createMeal.html')

@ui.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    error = None
    if request.method == 'POST':
        if form.validate():
            try:
                enc_pw = bcrypt.generate_password_hash(form.password.data)
                manage.users.register_user(form.username.data, enc_pw)
            except manage.users.UserExistsError:
                error = 'Username taken.'
            else:
                return redirect(url_for('.login'))
        else:
            error = 'Not registered.'
    return render_template('register.html', form=form, error=error)

@ui.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        user = User.by_id(session['user_id'])
        if user and user.is_authenticated():
            return redirect(url_for('.info'))
    form = LoginForm(request.form)
    error = None
    if request.method == 'POST':
        if form.validate():
             login_user(form.user)
             session['user_id'] = str(form.user.id)
             return redirect(url_for('.info'))
        else:
            error = 'Invalid username/password.'
    return render_template('login.html', form=form, error=error)

@ui.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
