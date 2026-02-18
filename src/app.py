from flask import Flask, Blueprint


app = Flask(__name__)

def create_app():
    app = Flask(__name__)

    # register blueprint
    from src.main import main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    return app