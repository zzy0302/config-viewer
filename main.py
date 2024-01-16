from flask import Flask
from config_viewer_frontend.views import *
import requests
app = Flask(__name__)

flask_debug = app.config['DEBUG']
debug_pnpm = True
if (flask_debug and debug_pnpm):
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    async def index(path=None):
        response = await get_pnpm_dev(request.path)
        return response.content, response.status_code, response.headers.items()
else:
    app.register_blueprint(vite_bp, url_prefix='/')


async def get_pnpm_dev(path):
    print("dev path: " + path, flush=True)
    baseUrl = 'http://localhost:5001'
    if path == '/':
        path = '/index.html'
    if path:
        baseUrl += path
    response = requests.get(baseUrl)
    print("dev path: " + path + " response: " +
          response.text[:100], flush=True)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, reload=True)
