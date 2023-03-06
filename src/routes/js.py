from flask import Blueprint, Response

js_route = Blueprint("js_api", __name__, url_prefix='/js')


@js_route.route('/<filename>', methods=['GET'])
def get_css_resource(filename: str):
    with open(f"views/js/{filename}", 'r') as fs:
        data = fs.read()
    return Response(data, mimetype="application/js")
