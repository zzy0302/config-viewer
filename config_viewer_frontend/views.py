from flask import Blueprint, Flask, request
vite_bp = Blueprint('frontend', __name__,
                    static_folder='dist', static_url_path='/')


@vite_bp.route('/', defaults={'path': ''})
@vite_bp.route('/<path:path>')
def index(path=None):
    return vite_bp.send_static_file('index.html')
