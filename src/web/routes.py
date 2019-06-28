from flask import (
    Blueprint,
    render_template
)
from .views import (
    index,
    login,
    callback,
    community_page,
    album_page,
    task_page,
    task_post,
    file_download,
    support_page
)
from auth.before_request import before_request

web_bp = Blueprint('web', __name__, template_folder='./templates')

web_bp.before_app_request(before_request)

web_bp.add_url_rule('/', 'index', index, methods=['GET'])
web_bp.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
web_bp.add_url_rule('/callback', 'callback', callback, methods=['GET', 'POST'])

web_bp.add_url_rule('/tasks', 'tasks', task_page, methods=['GET'])

web_bp.add_url_rule('/community', 'community', community_page, methods=['GET'])
web_bp.add_url_rule('/community/<community_id>/albums', 'albums', album_page, methods=['GET'])
web_bp.add_url_rule('/community/<community_id>/albums/<album_id>', 'task_post', task_post, methods=['GET'])

web_bp.add_url_rule('/support', 'support', support_page, methods=['GET'])


web_bp.add_url_rule('/files/<task_id>', 'file_download', file_download, methods=['GET'])


@web_bp.errorhandler(404)
def not_found_page(e):
    return render_template('not_found_page.html'), 404
