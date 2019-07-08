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
    start_time = fields.Timestamp(default=None)
    end_time = fields.Timestamp(default=None)


class SerializationSchema(ApiSchema):

    items = fields.Nested(NotificationSchema, many=True)
    totals = fields.Int()
    filters = fields.Nested(FiltersSchema)


class NotificationsGet(Resource):

    @login_required
    def get(self):
        filters = FiltersSchema().deserialize(self.request.args, unknown=EXCLUDE)
        user = self.g.user

        query_kwargs = {}

        if 'start_time' in filters:
            query_kwargs['created_at__gte'] = filters['start_time']

        if 'end_time' in filters:
            query_kwargs['created_at__lte'] = filters['end_time']

        notifications = Notification.objects(user=user).filter(**query_kwargs)
        items = notifications.skip(filters['start']).limit(filters['limit'])

        return SerializationSchema().serialize({'items': items, 'totals': len(items), 'filters': filters})
