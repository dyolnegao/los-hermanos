from flask import Blueprint, render_template, request, redirect, url_for
from flask_compass.extensions import db
from flask_compass.UsuarioModel import User
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

LoginController = Blueprint('LoginController', __name__)

@LoginController.route('/', methods=['GET', 'POST'])
def fazerLogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        error_message = ''

        if not user or not check_password_hash(user.password, password):
            error_message = 'Senha errada'

        if not error_message:
            login_user(user)
            return redirect(url_for('main.home'))

    return render_template('LoginView.html')

