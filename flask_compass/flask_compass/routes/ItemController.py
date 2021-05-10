from flask import Blueprint, render_template, request, redirect, url_for
from flask_compass.extensions import db
from flask_compass.ItemModel import Item
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

ItemController = Blueprint('ItemController', __name__)

@ItemController.route('/cadastraItem', methods=['GET', 'POST'])
def addItem():
    if request.method == 'POST':
        tipo = request.form['tipo']
        titulo = request.form['titulo']
        diretor = request.form['diretor']
        pais = request.form['pais']
        ano = request.form['ano']
        genero = request.form['genero']

        item = Item(
            tipo=tipo, 
            titulo=titulo,
            diretor=diretor,  
            pais=pais,
            ano=ano,
            genero=genero
        )

        db.session.add(item)
        db.session.commit()

        return redirect(url_for('main.home'))

    return render_template('ItemView.html')