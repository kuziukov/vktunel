import json
from extentions.redis import session_store
from utils import (
    generate_uuid1
)


class SessionData:

    def __get__(self, obj, objtype):
        if obj._data is None:
            data = session_store.get(obj.key)
            if data is not None:
                obj._data = json.loads(data)
        return obj._data

    def __set__(self, obj, value):
        obj._data = value


class Session(object):

    data = SessionData()

    def __init__(self, key):
        self._key = key
        self.data = None

    def is_exists(self):
        return session_store.exists(self.key)

    def destroy(self):
        return session_store.delete(self.key)

    def save(self, expires_in=None):
        if expires_in is None:
            ttl = session_store.ttl(self.key)
            # -1 key without ttl
            if ttl != -1:
                expires_in = ttl
        result = session_store.set(self.key, json.dumps(self.data), expires_in)
        return result

    @property
    def key(self):
        return self._key.decode('utf-8') if isinstance(self._key, bytes) else self._key


def create_session(users, expires_in) -> Session:
    session_id = generate_uuid1()
    session = Session(session_id)
    session.data = {
        'access_token': users.access_token,
        'expires_in': users.expires_in,
        'user_id': users.user_id
    }
    expires_in = 500 if expires_in == 0 else expires_in
    session.save(expires_in=expires_in)
    return session


