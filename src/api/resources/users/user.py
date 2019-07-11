from api.auth.decorators import login_required
from api.resources.users.schemas import UserSchema
from cores.rest_core import Resource


class UserGet(Resource):

    @login_required
    def get(self):
        user = self.g.user
        return UserSchema().serialize(user)
