from flask import Blueprint
from cores.rest_core import Api

from .resources.notification import (
    NotificationsGet,
    NotificationUpdate,
    NotificationDelete
)
from .resources.task import (
    TasksGet,
    TasksTest,
    TasksPost
)
from .resources.subscription import (
    FcmSubscriptionPost
)
from .resources.authorization import (
    AuthorizationCode
)
from .resources.users import (
    UserGet
)
from .resources.community import (
    CommunityGet
)
from .resources.album import (
    AlbumGet
)

api_bp = Blueprint('api', __name__, url_prefix='/v1.0', template_folder='./templates')
api = Api(api_bp)


api.add_resource(AuthorizationCode, '/authorization/code')

api.add_resource(CommunityGet, '/community')
api.add_resource(AlbumGet, '/community/<string:community_id>/albums')
api.add_resource(TasksPost, '/community/<string:community_id>/albums/<string:album_id>')

api.add_resource(NotificationsGet, '/notifications')
api.add_resource(NotificationUpdate, '/notification/<string:notification_id>')
api.add_resource(NotificationDelete, '/notification/<string:notification_id>')

api.add_resource(TasksGet, '/tasks')
api.add_resource(TasksTest, '/tasks')

api.add_resource(FcmSubscriptionPost, '/subscription/fcm')

api.add_resource(UserGet, '/users')
