from api.auth.decorators import login_required
from api.resources.profile.schemas import ProfileSchema
from cores.rest_core import Resource
from models import Notification, NotificationsData


class PlanDelete(Resource):
    @login_required
    def delete(self):
        user = self.g.user

        if 'subscription' in user:
            if user.subscription.paid is True:
                notification = Notification()
                notification.user = user
                notification.type = 'PlanDeleted'
                notification.parent = NotificationsData()
                notification.parent.subscription = user.subscription
                notification.save()

        del user.subscription
        user.save()
        return ProfileSchema().serialize(user)
