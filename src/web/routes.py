from flask import Blueprint
from .views.index import index

web_bp = Blueprint('web', __name__, template_folder='./templates')

web_bp.add_url_rule('/', 'index', index, methods=['GET'])
