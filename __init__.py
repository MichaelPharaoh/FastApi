from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    # create and configure the app
    app = Flask(__name__)
    
    # configure SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db' # use your SQLite database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initialize extensions
    db.init_app(app)

    # Set up Flask-Migrate
    migrate = Migrate(app, db)

    # Import your application routes and register blueprints
    from myapp import routes

    app.register_blueprint(routes.bp)

    return app

