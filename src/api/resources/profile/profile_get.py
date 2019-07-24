from api.auth.decorators import login_required
from api.resources.profile.schemas import ProfileSchema
from cores.rest_core import Resource


class ProfileGet(Resource):

    @login_required
    def get(self):
        user = self.g.user
        return ProfileSchema().serialize(user)
