from flask import Blueprint, send_file

img_route = Blueprint("img_api", __name__, url_prefix='/img/')


@img_route.route('/<filename>', methods=['GET'])
def get_css_resource(filename: str):
    return send_file(f"../views/img/{filename}", mimetype='image/png')
