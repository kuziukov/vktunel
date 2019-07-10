from flask import Blueprint
from cores.rest_core import Api

from .resources.notification import (
    NotificationsGet,
    NotificationUpdate,
    NotificationDelete
)
from .resources.task import (
    TasksGet,
    TasksTest
)
from .resources.subscription import (
    FcmSubscriptionPost
)
from .resources.authorization.authorization_access import (
    AuthorizationAccessToken
)


api_bp = Blueprint('api', __name__, url_prefix='/v1.0', template_folder='./templates')

api = Api(api_bp)

api.add_resource(AuthorizationAccessToken, '/authorization/token')

api.add_resource(NotificationsGet, '/notifications')
api.add_resource(NotificationUpdate, '/notification/<string:notification_id>')
api.add_resource(NotificationDelete, '/notification/<string:notification_id>')

api.add_resource(TasksGet, '/tasks')
api.add_resource(TasksTest, '/tasks')

api.add_resource(FcmSubscriptionPost, '/subscription/fcm')
