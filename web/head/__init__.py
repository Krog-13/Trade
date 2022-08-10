from flask import Blueprint

bp = Blueprint('main', __name__)

from web.head import routes