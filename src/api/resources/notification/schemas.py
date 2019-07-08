from cores.marshmallow_core import (
    ApiSchema
)
from cores.marshmallow_core import fields
from api.resources.task.schemas import TaskSchema


class NotificationsDataSchema(ApiSchema):

    task = fields.Nested(TaskSchema)


class UserSchema(ApiSchema):

    id = fields.Str(default=None)
    name = fields.Str(default=None)


class NotificationSchema(ApiSchema):

    id = fields.Str(default=None)
    user = fields.Nested(UserSchema, default=None)
    type = fields.Str(default=None)
    created_at = fields.Timestamp()
    parent = fields.Nested(NotificationsDataSchema, default=None)
