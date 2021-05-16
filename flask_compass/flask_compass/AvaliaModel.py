from .extensions import db 

class AvaliaItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comentario = db.Column(db.String(300))
    like = db.Column(db.Boolean)

