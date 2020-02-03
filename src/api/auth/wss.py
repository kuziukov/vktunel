import json
from extentions.redis import notification_store
from utils import (
    generate_uuid1
)


class WSSessionData:

    def __get__(self, obj, objtype):
        if obj._data is None:
            data = notification_store.get(obj.key)
            if data is not None:
                obj._data = json.loads(data)
        return obj._data

    def __set__(self, obj, value):
        obj._data = value


class WSSession(object):

    data = WSSessionData()

    def __init__(self, key):
        self._key = key
        self.data = None

    def is_exists(self):
        return notification_store.exists(self.key)

    def destroy(self):
        return notification_store.delete(self.key)

    def save(self, expires_in=None):
        if expires_in is None:
            ttl = notification_store.ttl(self.key)
            # -1 key without ttl
            if ttl != -1:
                expires_in = ttl
        result = notification_store.set(self.key, json.dumps(self.data), expires_in)
        return result

    @property
    def key(self):
        return self._key.decode('utf-8') if isinstance(self._key, bytes) else self._key


def create_ws_session(users) -> WSSession:
    session_id = generate_uuid1()
    session = WSSession(session_id)
    session.data = {
        'user_id': str(users.id)
    }
    session.save(expires_in=120)
    return session


