from datetime import datetime, timedelta
from config import (
    SECRET_KEY
)
import jwt


class JWT(object):
    def __init__(self, key):
        self.key = key
        self.data = None


class Token(object):

    _alg = 'HS256'

    def __init__(self, session_id, user_id):
        self._session_id = session_id
        self._user_id = user_id
        self._exp = None
        self._scopes = ['user']

    @property
    def user_id(self):
        return self._user_id

    @property
    def session_id(self):
        return self._session_id

    @property
    def scopes(self):
        return self._scopes

    def setAlghoritm(self, alg) -> None:
        self._alg = alg

    def setScopes(self, scopes):
        self._scopes = scopes

    def generate(self, expires_in, secret=SECRET_KEY) -> (int, str):
        print(expires_in)
        expires_in = datetime.utcnow() + timedelta(seconds=expires_in)
        payload_access = {
            'id': self._session_id,
            'exp': expires_in,
            'user_id': str(self._user_id),
            'scopes': self.scopes
        }
        return jwt.encode(payload_access, secret, algorithm=self._alg), expires_in

    @classmethod
    def parse(cls, token, secret=SECRET_KEY):
        payload = jwt.decode(token, secret, algorithms=[cls._alg])
        token = cls(payload['id'], payload['user_id'])
        expires_in = payload['exp']
        if 'scopes' in payload:
            token._scopes = payload['scopes']
        return token, expires_in

    def check(self):
        return True if self.user_id and self.session_id else False


