from api.auth.decorators import login_required
from api.resources.profile.schemas import ProfileUserSchema
from cores.rest_core import (
    Resource,
    APIException,
    codes
)
from cores.vk import API


class ProfileException(APIException):

    @property
    def message(self):
        return 'Profile exception, please try again'

    code = codes.BAD_REQUEST


class ProfileGets(Resource):

    @login_required
    def get(self, profile_id):

        user = self.g.user
        api = API(user.access_token, v=5.95)
        try:
            response = api.users.get(user_ids=profile_id)[0]
        except Exception:
            raise ProfileException()

        return ProfileUserSchema().serialize(response)
