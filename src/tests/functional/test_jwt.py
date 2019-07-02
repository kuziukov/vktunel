from datetime import datetime, timezone
from auth import Token


class TestToken(object):

    def test_generate(self):

        token = Token('session_id', 'user_id')
        expires_in = 2629744
        access_token, expires_in = token.generate(expires_in)
        assert access_token
        assert expires_in > datetime.utcnow()

    def test_parse(self):
        token = Token('session_id', 'user_id')
        expires_in = 2629744
        access_token, expires_in = token.generate(expires_in)

        response, expires_in_after = Token.parse(access_token)

        assert response.session_id == 'session_id'
        assert response.user_id == 'user_id'
        assert type(expires_in_after) == int
        assert expires_in_after == int(expires_in.replace(tzinfo=timezone.utc).timestamp())

