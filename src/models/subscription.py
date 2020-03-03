import datetime
from mongoengine import (
    Document,
    DateTimeField,
    BooleanField,
    ReferenceField,
    signals,
    Q
)

from .users import Users
from .plan import Plan


class Subscription(Document):
    user = ReferenceField(Users, required=True)
    plan = ReferenceField(Plan, required=True)
    paid = BooleanField(required=True, default=False)
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    expired_on = DateTimeField(required=True)

    meta = {
        'collection': 'subscription'
    }

