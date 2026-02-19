from flask import Flask, Blueprint
import os


app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

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