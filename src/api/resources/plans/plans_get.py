from api.resources.plans.schemas import PlansSchema
from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields
from models.plan import Plan
from cores.rest_core import Resource


class SerializationSchema(ApiSchema):

    items = fields.Nested(PlansSchema, many=True)
    totals = fields.Int()


class PlansGet(Resource):

    def get(self):
        plans = Plan.objects(active=True)
        return SerializationSchema().serialize({'items': plans, 'totals': len(plans)})
