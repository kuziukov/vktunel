from api.auth.decorators import login_required
from api.auth.wss import create_ws_session
from api.resources.stream.schemas import StreamSchema
from cores.rest_core import Resource


class StreamGet(Resource):

    @login_required
    def get(self):
        user = self.g.user
        session = create_ws_session(users=user)
        response = {
            'key': session.key,
            'endpoint': 'stream.wlusm.ru'
        }
        return StreamSchema().serialize(response)
