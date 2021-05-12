from flask import Flask 

from .commands import create_tables
from .UsuarioModel import User
from .ItemModel import Item
from .extensions import db, login_manager
from flask_compass.routes.main import main
from flask_compass.routes.LoginController import LoginController
from flask_compass.routes.AcessoController import AcessoController
from flask_compass.routes.ItemController import ItemController
from flask_compass.routes.AvaliaController import AvaliaController

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.secret_key = 'oisadjva9sd8uvasdvojasasdfasdfasdf'

    app.config.from_pyfile(config_file)

    db.init_app(app)

    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    app.register_blueprint(LoginController)
    app.register_blueprint(AcessoController)
    app.register_blueprint(ItemController)
    app.register_blueprint(AvaliaController)
    app.register_blueprint(main)

    app.cli.add_command(create_tables)

    return app