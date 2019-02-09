from app.doc import TEMPLATE
from config import Config, ProdConfig, TestConfig
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flasgger import Swagger

db = SQLAlchemy(session_options={'autoflush': False})
jwt = JWTManager()


def create_app(config: Config):
    app_ = Flask(__name__)
    app_.config.from_object(config)

    db.init_app(app_)
    jwt.init_app(app_)

    with app_.app_context():
        from app import model
        # if config is not ProdConfig:
        #     db.drop_all()
        db.create_all()

    from app.view import Router
    Swagger(template=TEMPLATE).init_app(app_)
    Router().init_app(app_)

    return app_


