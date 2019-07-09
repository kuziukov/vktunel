from mongoengine import NotUniqueError

from api.auth.decorators import login_required
from api.resources.subscription.schemas import FCMSubscriptionSchema
from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields
from models.subscription_fcm import FcmSubscription
from cores.rest_core import Resource, APIException, codes


class FcmTokenException(APIException):

    @property
    def message(self):
        return 'Sorry, fcm token already exists.'

    code = codes.BAD_REQUEST


class KeysSchema(ApiSchema):
    p256dh = fields.Str(required=True)
    auth = fields.Str(required=True)


class DeserializationSchema(ApiSchema):

    endpoint = fields.Str(required=True)
    expirationTime = fields.Str(required=True, allow_none=True)
    keys = fields.Nested(KeysSchema, required=True)


class FcmSubscriptionPost(Resource):

    @login_required
    def post(self):
        user = self.g.user
        data = DeserializationSchema().deserialize(self.request.json)

        subscription = FcmSubscription()
        subscription.subscription = data
        subscription.user = user

        try:
            subscription.save()
        except NotUniqueError:
            raise FcmTokenException()

        return FCMSubscriptionSchema().serialize(subscription)
