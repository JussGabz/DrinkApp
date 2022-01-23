from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


# init sqlachemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/drinkapp"

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import Users

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))


    # blueprint for auth routes in our app
    from .auth import auth

    app.register_blueprint(auth)

    # blueprint for non-auth parts of app
    from .main import main

    app.register_blueprint(main)

    return app
