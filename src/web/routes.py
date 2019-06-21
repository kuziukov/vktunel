from flask import Blueprint
from .views.index import index
from .views.login import login
from .views.callback import callback

web_bp = Blueprint('web', __name__, template_folder='./templates')

web_bp.add_url_rule('/', 'index', index, methods=['GET'])
web_bp.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
web_bp.add_url_rule('/callback', 'callback', callback, methods=['GET', 'POST'])
