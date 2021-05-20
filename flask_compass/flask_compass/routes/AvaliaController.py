from flask_sqlalchemy.utils import engine_config_warning
from flask_compass import Flask
from flask_compass.routes.ItemController import ItemController
from flask_compass.ItemModel import Item
from flask import Blueprint, render_template, request, redirect, url_for
from flask_compass.extensions import db
from flask_compass.AvaliaModel import AvaliaItem

AvaliaController = Blueprint('avalia', __name__)
    
@AvaliaController.route('/avalia', methods=['GET', 'POST'])
def avalia(item_id):
    
    item = Item.query.get_or_404(item_id)

    if request.method == 'POST':
        AvaliaItem.avaliacao = request.form['avaliacao']
        AvaliaItem.nota = request.form['nota']
        AvaliaItem.like = request.form['like']
        db.session.commit()

        return redirect(url_for('AvaliaView.html'))

    context = {
        'item' : item
    }

    return render_template('AvaliaView.html', **context)

@AvaliaController.route('/item/<int:item_id>')
def item(item_id):
    item = Item.query.get_or_404(item_id)

    context = {
        'item' : item
    }

    return render_template('AvaliaView.html', **context)

@AvaliaController.route('/')
def index():
    itens = Item.query.all()

    context = {
        'itens' : itens
    }

    return render_template('home.html', **context)