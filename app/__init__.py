from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from app.admin import views as admin_views
    from app.home import views as home_views
    app.register_blueprint(home_views.home)
    app.register_blueprint(admin_views.admin)
    return app
