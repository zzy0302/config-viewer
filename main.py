from flask import Flask
from config_viewer_frontend.views import *
app = Flask(__name__)
app.register_blueprint(vite_bp, url_prefix='/')


if __name__ == '__main__':
    app.run(debug=True)