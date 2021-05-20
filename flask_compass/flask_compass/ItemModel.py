from .extensions import db 

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50))
    titulo = db.Column(db.String(100))
    diretor = db.Column(db.String(50))
    pais = db.Column(db.String(50))
    ano = db.Column(db.String(4))
    genero = db.Column(db.String(100))
    avaliacao = db.Column(db.String(300))
    nota = db.Column(db.Integer)
    like = db.Column(db.Boolean)

