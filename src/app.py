from flask import Flask

from src.routes import init_blueprints


def create_app():
    __app = Flask(__name__)
    init_blueprints(__app)
    return __app