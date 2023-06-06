from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    Migrate(app, db)

    from . import models
    from .routes import bp

    app.register_blueprint(bp)

    return app

