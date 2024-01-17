from flask import Blueprint
from tasks import *

apis_bp = Blueprint('apis', __name__)
# q: how to import flask app from main.py?
# a: https://stackoverflow.com/questions/1944569/how-do-i-import-modules-in-flask
@apis_bp.route('/add/')
def addone():
    return add(2,3)
