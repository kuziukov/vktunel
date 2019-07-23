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
    TaskPost
)
from .resources.subscription import (
    FcmSubscriptionPost
)
from .resources.authorization import (
    AuthorizationCode
)
from .resources.profile import (
    ProfileGet
)
from .resources.community import (
    CommunitiesGet
)
from .resources.album import (
    CommunityAlbumsGet
)

api_bp = Blueprint('api', __name__, url_prefix='/v1.0', template_folder='./templates')
api = Api(api_bp)

# Authorization
api.add_resource(AuthorizationCode, '/authorization/code')

# Community
api.add_resource(CommunitiesGet, '/communities')
# community/{communityId}

# Albums
api.add_resource(CommunityAlbumsGet, '/community/<string:community_id>/albums')
# /profile/<string:profile_id>/albums


# Notifications
api.add_resource(NotificationsGet, '/notifications')
api.add_resource(NotificationUpdate, '/notification/<string:notification_id>')
api.add_resource(NotificationDelete, '/notification/<string:notification_id>')

api.add_resource(TasksGet, '/tasks')
api.add_resource(TaskPost, '/tasks')

api.add_resource(FcmSubscriptionPost, '/subscription/fcm')

api.add_resource(ProfileGet, '/profile')
