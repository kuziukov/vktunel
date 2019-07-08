from flask import Blueprint
from rest_core import Api

from .resources.notification import (
    NotificationsGet,
    NotificationUpdate
)


api_bp = Blueprint('api', __name__, url_prefix='/v1.0', template_folder='./templates')

api = Api(api_bp)

api.add_resource(NotificationsGet, '/notifications')
api.add_resource(NotificationUpdate, '/notification/<string:notification_id>')