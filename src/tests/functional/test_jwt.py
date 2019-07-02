from datetime import datetime
from auth import Token


class TestToken(object):

    def test_generate(self):

        token = Token('session_id', 'user_id')
        expires_in = 2629744
        access_token, expires_in = token.generate(expires_in)
        assert access_token
        assert expires_in > datetime.utcnow()

