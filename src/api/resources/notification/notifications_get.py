from marshmallow import EXCLUDE
from marshmallow.validate import Range
from api.auth.decorators import login_required
from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields
from cores.rest_core import Resource
from .schemas import NotificationSchema
from models.notification import Notification


class FiltersSchema(ApiSchema):

    start = fields.Int(default=None, missing=0, validate=Range(min=0))
    limit = fields.Int(default=None, missing=50, validate=Range(min=0))


class SerializationSchema(ApiSchema):

    items = fields.Nested(NotificationSchema, many=True)
    totals = fields.Int()
    filters = fields.Nested(FiltersSchema)


class NotificationsGet(Resource):

    @login_required
    def get(self):
        filters = FiltersSchema().deserialize(self.request.args, unknown=EXCLUDE)
        user = self.g.user
        notifications = Notification.objects(user=user)
        items = notifications.skip(filters['start']).limit(filters['limit'])

        return SerializationSchema().serialize({'items': items, 'totals': len(items), 'filters': filters})
