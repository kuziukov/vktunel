from api.auth.decorators import login_required
from api.resources.community.schemas import CommunitySchema
from cores.rest_core import Resource, APIException, codes
from cores.vk import API


class CommunityException(APIException):

    @property
    def message(self):
        return 'Community exception, please try again'

    code = codes.BAD_REQUEST


class CommunityGet(Resource):

    @login_required
    def get(self, community_id):
        user = self.g.user
        api = API(user.access_token, v=5.95)
        try:
            response = api.groups.getById(group_id=community_id)[0]
        except Exception:
            raise CommunityException()

        return CommunitySchema().serialize(response)
