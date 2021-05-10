from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from .extensions import db 

#CriarUsuario
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(100))
    cidade = db.Column(db.String(50))
    estado = db.Column(db.String(50))
    password = db.Column(db.String(100))

    @property
    def unhashed_password(self):
        raise AttributeError('Não foi possível criptografar a senha!')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password)
