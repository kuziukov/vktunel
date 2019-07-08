from mongoengine import (
    Document,
    StringField,
    DateTimeField,
    ReferenceField,
    EmbeddedDocumentField,
    EmbeddedDocument,
    BooleanField
)
from datetime import datetime
from .users import Users
from .tasks import Tasks


class NotificationsData(EmbeddedDocument):

    task = ReferenceField(Tasks)


class Notification(Document):
    user = ReferenceField(Users)
    type = StringField(default=None)
    created_at = DateTimeField(default=datetime.utcnow)
    parent = EmbeddedDocumentField(NotificationsData)

    meta = {
        'collection': 'notifications'
    }
