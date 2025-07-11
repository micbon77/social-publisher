from flask import Flask
from flask_cors import CORS
from models.db import init_db

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_pyfile('../.env')
    init_db(app)

    from app.routes import api
    app.register_blueprint(api, url_prefix="/api")

    return app
