from flask import Flask
from .config import Config
from .extensions import db, migrate
from app.entrega.models import entrega_api
from app.pedido.models import item_api
from app.user.models import user_api


def create_app():
    
    app=Flask(__name__)
    app.config.from_object(Config)
    app.debug=True

    db.init_app(app)
    migrate.init_app(app,db)
    
    app.register_blueprint(entrega_api)
    app.register_blueprint(item_api)
    app.register_blueprint(user_api)
    
    
    return app
