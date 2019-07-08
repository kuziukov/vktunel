from api.auth.decorators import login_required
from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields
from cores.rest_core import Resource
from .schemas import NotificationSchema
from models.notification import Notification


class SerializationSchema(ApiSchema):

    items = fields.Nested(NotificationSchema, many=True)
    totals = fields.Int()


class NotificationsGet(Resource):

    @login_required
    def get(self):
        user = self.g.user
        notifications = Notification.objects(user=user)

        return SerializationSchema().serialize({'items': notifications, 'totals': notifications.count()})
