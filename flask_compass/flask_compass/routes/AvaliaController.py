from flask_sqlalchemy.utils import engine_config_warning
from flask_compass.routes.ItemController import ItemController
from flask_compass.ItemModel import Item
from flask import Blueprint, render_template, request, redirect, url_for
from flask_compass.extensions import db
from flask_compass.AvaliaModel import AvaliaItem

AvaliaController = Blueprint('avaliaItem', __name__)
    
@AvaliaController.route('/avaliaItem', methods=['GET', 'POST'])
def avalia(item_id):
    
    item = ItemController.query.get_or_404(item_id)

    if request.method == 'POST':
        item.avaliacao = request.form['avaliacao']
        item.nota = request.form['nota']
        item.like = request.form['like']
        db.session.commit()

        return redirect(url_for('home'))

    context = {
        'item' : item
    }

    return render_template('AvaliaView.html', **context)

@AvaliaController.route('/avaliaItem', methods=['GET', 'POST'])
def index():
    itens = Item.query.all()

    context = {
        'itens' : itens
    }

    return render_template('AvaliaView.html', **context)