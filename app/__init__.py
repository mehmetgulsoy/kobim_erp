from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from ayarlar import Congfig

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(ayar_class=Congfig):
    app = Flask(__name__)
    app.config.from_object(ayar_class)
    db.init_app(app)
    bootstrap.init_app(app)

    from app.malzeme import bp as mlz_bp
    app.register_blueprint(mlz_bp, url_prefix='/mlz')

    return app
