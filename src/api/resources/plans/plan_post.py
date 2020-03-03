import datetime
from api.auth.decorators import login_required
from api.resources.plans.schemas import SubscriptionSchema
from cores.rest_core import (
    Resource,
    APIException,
    codes
)
from models import (
    Notification,
    NotificationsData,
    Plan,
    Subscription
)


class PlanException(APIException):

    @property
    def message(self):
        return 'Plan does not exist, please use correct plan id'

    code = codes.BAD_REQUEST


class PlanPost(Resource):

    @login_required
    def post(self, plan_id):
        user = self.g.user
        try:
            plan = Plan.objects.get(id=plan_id)
        except Exception as e:
            raise PlanException()

        subscription = Subscription()
        subscription.user = user
        subscription.plan = plan
        subscription.expired_on = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        subscription.paid = True if plan.price == 0 else False

        try:
            subscription.save()
        except Exception as e:
            raise PlanException()

        user.subscription = subscription
        user.save()

        notification = Notification()
        notification.user = user
        notification.type = 'PlanChanged'
        notification.parent = NotificationsData()
        notification.parent.subscription = subscription
        notification.save()

        return SubscriptionSchema().serialize(subscription)
