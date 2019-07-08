from flask import Blueprint
from rest_core import Api

from .resources.notification import (
    NotificationsGet
)


api_bp = Blueprint('api', __name__, url_prefix='/v1.0', template_folder='./templates')

api = Api(api_bp)

api.add_resource(NotificationsGet, '/notifications')