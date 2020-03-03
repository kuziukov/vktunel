from mongoengine import (
    Document,
    StringField,
    ReferenceField
)


class Users(Document):
    user_id = StringField(required=True, unique=True)
    name = StringField(required=True)
    access_token = StringField(required=True)
    subscription = ReferenceField('Subscription')

    meta = {
        'collection': 'profile'
    }
