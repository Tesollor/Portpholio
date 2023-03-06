from flask import Flask

from src.routes.css import css_route
from src.routes.img import img_route
from src.routes.js import js_route
from src.routes.page import page_route


def init_blueprints(app: Flask):
    app.register_blueprint(css_route)
    app.register_blueprint(js_route)
    app.register_blueprint(img_route)
    app.register_blueprint(page_route)