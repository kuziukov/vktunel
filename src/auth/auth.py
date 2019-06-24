from .session import (
    SessionManager,
    Session
)
from auth.jwt import Token


class Auth(object):
    def __init__(self):
        pass

    @staticmethod
    def sign_in(user) -> dict:
        session = SessionManager.create_session(users=user, expires_in=user.expires_in)
        access_token = Token.generate(user.expires_in)
        # generate jwt token

    @staticmethod
    def is_signed_in(jwt):
        token, expires_in = Token.parse(jwt)


