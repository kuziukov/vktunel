from mongoengine import DoesNotExist, ValidationError
from werkzeug.exceptions import NotFound
from api.auth.decorators import login_required
from api.resources.notification.schemas import NotificationSchema
from models.notification import Notification
from rest_core import Resource


class NotificationDelete(Resource):
    @login_required
    def delete(self, notification_id):
        user = self.g.user
        try:
            notify = Notification.objects.get(id=notification_id, user=user)
        except (DoesNotExist, ValidationError):
            raise NotFound()

        notify.delete()

        return NotificationSchema().serialize(notify)
