import datetime
from mongoengine import Q
from api.auth import login_required
from api.resources.plans.schemas import SubscriptionSchema
from cores.rest_core import Resource
from models.subscription import Subscription


class PlanGet(Resource):

    @login_required
    def get(self):
        user = self.g.user
        now = datetime.datetime.utcnow()
        plans = Subscription.objects(user=user).filter(
            (Q(expired_on__gte=now))
        ).order_by("-plan").limit(-1).first()
        return SubscriptionSchema().serialize(plans)
