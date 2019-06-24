from flask import Blueprint
from .views.index import index
from .views.login import login
from .views.callback import callback
from .views.album_page import album_page

web_bp = Blueprint('web', __name__, template_folder='./templates')

web_bp.add_url_rule('/', 'index', index, methods=['GET'])
web_bp.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
web_bp.add_url_rule('/callback', 'callback', callback, methods=['GET', 'POST'])
web_bp.add_url_rule('/photos', 'photos', album_page, methods=['GET'])

web_bp.add_url_rule('/community', 'community', None, methods=['GET'])
web_bp.add_url_rule('/community/<community_id>/albums', 'albums', None, methods=['GET'])
