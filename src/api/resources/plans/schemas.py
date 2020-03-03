from cores.marshmallow_core import (
    ApiSchema
)
from cores.marshmallow_core import fields


class PlansSchema(ApiSchema):
    id = fields.ObjectID()
    title = fields.Str()
    desc = fields.Str()
    price = fields.Int()
    limits = fields.Dict()


class SubscriptionSchema(ApiSchema):
    id = fields.ObjectID()
    plan = fields.Nested(PlansSchema)
    paid = fields.Bool(default=False)
    created_at = fields.Timestamp(default=None)
    expired_on = fields.Timestamp(default=None)