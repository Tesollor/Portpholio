from flask import Blueprint, Response

css_route = Blueprint("css_api", __name__, url_prefix='/css')


@css_route.route('/<filename>', methods=['GET'])
def get_css_resource(filename: str):
    with open(f"views/css/{filename}", 'r') as fs:
        data = fs.read()

    return Response(data, mimetype="text/css")
