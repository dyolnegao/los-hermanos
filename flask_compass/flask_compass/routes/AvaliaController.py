from flask import Blueprint, render_template, request, redirect, url_for
from flask_compass.extensions import db
from flask_compass.AvaliaModel import AvaliaItem

AvaliaController = Blueprint('avaliaItem', __name__)

@AvaliaController.route('/avaliaItem', methods=['GET', 'POST'])
def addAvaliacao():
    if request.method == 'POST':
        comentario = request.form['comentario']
        
        avaliacao = Avaliacao(
            comentario=comentario,             
        )

        db.session.add(avaliacao)
        db.session.commit()

        return redirect(url_for('AvaliaView.html'))

    return render_template('AvaliaView.html')

def addLike():
    if request.method == 'POST':
        like = request.button['like']
        
        like = Like(
            like=like,             
        )

        db.session.add(like)
        db.session.commit()

        return redirect(url_for('AvaliaView.html'))

    return render_template('AvaliaView.html')