from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields


class UserSchema(ApiSchema):

    id = fields.Str(default=None)
    name = fields.Str(default=None)
