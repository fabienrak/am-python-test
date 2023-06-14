import os

from flasgger import Swagger
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from src.utils.config import Config, DevelopmentConfig
from src.utils.swagger import swagger_config, template

db = SQLAlchemy()
db_migration = Migrate()

from src.services.TaskService import task_blueprint
from src.services.AuthService import auth_blueprint


def bootstrap_app():
    app = Flask(__name__)
    APP_CONFIG = os.getenv('APP_CONFIG', default=DevelopmentConfig)
    app.config.from_object(APP_CONFIG)

    SWAGGER_DOC = {
        'title': os.environ.get('SWAGGER_TITLE'),
        'uiversion': 3
    }

    Swagger(app, config=swagger_config, template=template)
    app_module(app)
    route_blueprint(app)

    with app.app_context():
        db.create_all()

        return app


def app_module(app):
    db.init_app(app)
    db_migration.init_app(app, db)
    from src.models.Task import Task
    from src.models.User import User


def route_blueprint(app):
    app.register_blueprint(task_blueprint)
    app.register_blueprint(auth_blueprint)
