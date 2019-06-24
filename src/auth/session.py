import json
from flask import current_app
from extentions.redis import session_store
from utils import (
    generate_uuid1
)


class Session(object):
    def __init__(self, key):
        self._key = key
        self.data = None
        self.store = session_store

    def is_exists(self):
        return self.store.exists(self.key)

    def destroy(self):
        return self.store.delete(self.key)

    def save(self, expires_in=None):
        if expires_in is None:
            ttl = self.store.ttl(self.key)
            # -1 key without ttl
            if ttl != -1:
                expires_in = ttl
        result = self.store.set(self.key, json.dumps(self.data), expires_in)
        return result

    @property
    def key(self):
        return self._key.decode('utf-8') if isinstance(self._key, bytes) else self._key


class SessionManager(object):
    @staticmethod
    def create_session(users, expires_in) -> Session:
        session_id = generate_uuid1()
        session = Session(session_id)
        session.data = {
            'access_token': users.access_token,
            'expires_in': users.expires_in,
            'user_id': users.user_id
        }
        expires_in = 5000 if expires_in == 0 else expires_in
        session.save(expires_in=expires_in)
        return session


