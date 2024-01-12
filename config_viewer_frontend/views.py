from flask import Blueprint

vite_bp = Blueprint('frontend', __name__, static_folder='dist', static_url_path='/')

@vite_bp.route('/')
def index():
    print('index app')
    return vite_bp.send_static_file('index.html')