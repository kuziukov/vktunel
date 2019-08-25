from mongoengine import (
    Document,
    StringField,
    ReferenceField
)
from models import Users


class FcmSubscription(Document):
    user = ReferenceField(Users, required=True)
    token = StringField(required=True, unique=True)

    meta = {
        'collection': 'fcm_subscriptions'
    }
