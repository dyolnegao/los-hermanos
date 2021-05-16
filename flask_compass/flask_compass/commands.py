import click
from flask.cli import with_appcontext
from .extensions import db
from .UsuarioModel import User
from .ItemModel import Item
from .AvaliaModel import AvaliaItem

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()