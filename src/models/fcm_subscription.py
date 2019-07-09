from mongoengine import (
    Document,
    StringField,
    ReferenceField,
    DictField
)
from models import Users


class FCMSubscription(Document):
    user = ReferenceField(Users, required=True)
    subscription = DictField(required=True, unique=True)

    meta = {
        'collection': 'fcm_subscriptions'
    }
