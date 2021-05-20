from .extensions import db 

class AvaliaItem(db.Model):
    avaliacaoId = db.Column(db.Integer, primary_key=True)
    comentario = db.Column(db.String(300))
    like = db.Column(db.Boolean)
    nota = db.Column(db.Integer)