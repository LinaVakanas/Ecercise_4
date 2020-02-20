from os.path import dirname, abspath, join

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig

db = SQLAlchemy()


def create_app(config_class=DevConfig):
    """Creates an application instance to run using settings from config.py
    :return: A Flask object"""

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dfdQbTOExternjy5xmCNaA'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CWD = dirname(abspath(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(CWD, 'rain_sqlite.db')

    # app.config.from_object(config_class)
    db.init_app(app)
    # The following is needed if you want to map classes to an existing database
    # from app.models import User, City, Forecast
    with app.app_context():
        db.Model.metadata.reflect(db.engine)
        # db.create_all()
    #
    # with app.app_context():
    #     db.init_app(app)


    # Register Blueprints
    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app

