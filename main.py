from flask import Flask
from config_viewer_frontend.views import *
from tasks import *
from apis import *
import requests

app = Flask(__name__)

flask_debug = app.config['DEBUG']
debug_pnpm = False
if (flask_debug and debug_pnpm):
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def index(path=None):
        if path.startswith('api'):
            return path
        response = get_pnpm_dev(request.path)
        return response.content, response.status_code, response.headers.items()
else:
    app.register_blueprint(vite_bp, url_prefix='/')

app.register_blueprint(apis_bp, url_prefix='/api')

def get_pnpm_dev(path):
    baseUrl = 'http://localhost:5051'
    if path == '/':
        path = '/index.html'
    if path:
        baseUrl += path
    response = requests.get(baseUrl)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5052, reload=True)
