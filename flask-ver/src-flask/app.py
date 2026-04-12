from flask import Flask, Blueprint
from flask_login import LoginManager
from bson import ObjectId
import os
from src.database.db import get_user_collection
from src.models.user import User


app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        try:
            _id = ObjectId(id)
        except Exception:
            return None
        
        users = get_user_collection()
        doc = users.find_one({"_id": _id})
        return User(doc) if doc else None

    # register blueprint
    from src.main import main_bp
    from src.auth import auth_bp
    from src.user import user_bp
    from src.pal_posts import pal_bp
    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(pal_bp, url_prefix='/')

    return app