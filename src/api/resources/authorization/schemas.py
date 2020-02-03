from cores.marshmallow_core import (
    ApiSchema,
    fields
)


class AuthorizationSchema(ApiSchema):

    access_token = fields.Str(default=None)
    expires_in = fields.Timestamp(default=None)


class DeserializationSchema(ApiSchema):

    code = fields.Str(required=True)


class VKDeserializationSchema(ApiSchema):

    access_token = fields.Str(required=True)
    expires_in = fields.Int(required=True)
    user_id = fields.Int(required=True)
    email = fields.Str(required=False)


class VKProfileSchema(ApiSchema):

    id = fields.Int(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
