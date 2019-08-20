from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields


class ProfileSchema(ApiSchema):

    id = fields.Str(default=None)
    name = fields.Str(default=None)


class ProfileUserSchema(ApiSchema):

    id = fields.Str(default=None)
    first_name = fields.Str(default=None)
    last_name = fields.Str(default=None)
