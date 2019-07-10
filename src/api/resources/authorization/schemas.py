from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields


class AuthorizationSchema(ApiSchema):

    access_token = fields.Str(default=None)