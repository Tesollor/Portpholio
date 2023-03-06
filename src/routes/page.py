from flask import Blueprint

page_route = Blueprint("page_api", __name__)


@page_route.route('/', methods=['GET'])
def get_css_resource():
    with open(f"views/index.html", 'r') as fs:
        data = fs.read()
    return data
