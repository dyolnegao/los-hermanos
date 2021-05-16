from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from flask_compass.extensions import db
from flask_compass.UsuarioModel import User

main = Blueprint('main', __name__)

@main.route('/home')
def home():
    return render_template('AvaliaView.html')

@main.route('/cadastro')
def cadastro():
    return render_template('ItemView.html')