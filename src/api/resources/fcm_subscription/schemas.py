from api.resources.notification.schemas import UserSchema
from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields


class FCMSubscriptionSchema(ApiSchema):

    id = fields.Str(default=None)
    user = fields.Nested(UserSchema, default=None)