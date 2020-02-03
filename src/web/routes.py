from flask import (
    Blueprint,
    render_template
)
from .views import (
    file_download
)


web_bp = Blueprint('web', __name__, template_folder='./templates')
web_bp.add_url_rule('/files/<task_id>', 'file_download', file_download, methods=['GET'])


@web_bp.errorhandler(404)
def not_found_page(e):
    return render_template('not_found_page.html'), 404
