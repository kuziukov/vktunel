from flask import Blueprint
from cores.rest_core import Api

from .resources.notification import (
    NotificationsGet,
    NotificationUpdate,
    NotificationDelete
)
from .resources.task import (
    TasksGet,
    TaskPost
)
from .resources.subscription import (
    SubscriptionPost
)
from .resources.authorization import (
    AuthorizationCode
)
from .resources.profile import (
    ProfileGet,
    ProfileGets
)
from .resources.community import (
    CommunitiesGet,
    CommunityGet
)
from .resources.album import (
    AlbumsGet,
)
from .resources.stream import (
    StreamGet
)
from .resources.utils import (
    UtilsLinkPost
)
from .resources.plans import (
    PlansGet,
    PlanPost,
    PlanGet,
    PlanUpdate,
    PlanDelete
)

api_bp = Blueprint('api', __name__, url_prefix='/v1.0', template_folder='./templates')
api = Api(api_bp)

# Authorization
api.add_resource(AuthorizationCode, '/authorization/code')

# Community
api.add_resource(CommunitiesGet, '/communities')
api.add_resource(CommunityGet, '/community/<string:community_id>')

# Albums
api.add_resource(AlbumsGet, '/albums/<string:object_id>')

# Notifications
api.add_resource(NotificationsGet, '/notifications')
api.add_resource(NotificationUpdate, '/notification/<string:notification_id>')
api.add_resource(NotificationDelete, '/notification/<string:notification_id>')

# Tasks
api.add_resource(TasksGet, '/tasks')
api.add_resource(TaskPost, '/tasks')

# Web Subscriptions
api.add_resource(SubscriptionPost, '/subscription')

# Profiles
api.add_resource(ProfileGet, '/profile')
api.add_resource(ProfileGets, '/profile/<string:profile_id>')

# Stream
api.add_resource(StreamGet, '/stream')

# Plans
api.add_resource(PlanGet, '/subscriptions')
api.add_resource(PlanDelete, '/subscription')
api.add_resource(PlansGet, '/plans')
api.add_resource(PlanPost, '/plan/<string:plan_id>')
api.add_resource(PlanUpdate, '/plan/<string:plan_id>')

# Utils
api.add_resource(UtilsLinkPost, '/utils/link')
