from api.auth.decorators import login_required
from api.resources.plans.plan_post import PlanException
from api.resources.plans.schemas import SubscriptionSchema
from cores.rest_core import Resource
from models import (
    Subscription
)


class PlanUpdate(Resource):

    @login_required
    def put(self, plan_id):
        user = self.g.user
        try:
            subcription = Subscription.objects.get(id=plan_id, user=user)
            subcription.paid = True
            subcription.save()
        except Exception as e:
            raise PlanException()

        return SubscriptionSchema().serialize(subcription)
