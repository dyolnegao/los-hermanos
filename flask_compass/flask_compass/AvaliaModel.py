from .extensions import db 

class AvaliaItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    avaliacao = db.Column(db.String(300))
    like = db.Column(db.Boolean)
    nota = db.Column(db.Integer)

    item_avaliado = db.relationship(
        'Item', 
        foreign_keys='item.avaliacao', 
        backref='avaliador', 
        lazy=True
    )


