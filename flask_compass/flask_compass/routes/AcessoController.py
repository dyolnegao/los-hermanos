from flask import Blueprint, render_template, request, redirect, url_for
from flask_compass.extensions import db
from flask_compass.UsuarioModel import User
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

AcessoController = Blueprint('AcessoController', __name__)

@AcessoController.route('/profile', methods=['GET', 'POST'])
def criarUsuario():
    if request.method == 'POST':
        name = request.form['nome']
        username = request.form['username']
        cidade = request.form['cidade']
        estado = request.form['estado']
        password = request.form['password']

        user = User(
            name=name, 
            username=username,
            cidade=cidade,  
            estado=estado,
            unhashed_password=password
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('LoginController.fazerLogin'))

    return render_template('AcessoView.html')