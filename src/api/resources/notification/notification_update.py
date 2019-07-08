from mongoengine import DoesNotExist, ValidationError
from werkzeug.exceptions import NotFound

from api.auth.decorators import login_required
from api.resources.notification.schemas import NotificationSchema
from marshmallow_core import fields, ApiSchema
from models.notification import Notification
from rest_core import Resource


class DeserializationSchema(ApiSchema):

    hide = fields.Bool()


class NotificationUpdate(Resource):

    @login_required
    def put(self, notification_id):
        user = self.g.user
        data = DeserializationSchema().deserialize(self.request.json)

        try:
            notify = Notification.objects.get(id=notification_id, user=user)
        except (DoesNotExist, ValidationError):
            raise NotFound()

        if 'hide' in data:
            notify.hide = data['hide']
        notify.save()

        return NotificationSchema().serialize(notify)
