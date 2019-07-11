from api.auth.decorators import login_required
from api.resources.task import TaskSchema
from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields
from models.tasks import Tasks
from cores.rest_core import Resource


class SerializationSchema(ApiSchema):

    items = fields.Nested(TaskSchema, many=True)
    totals = fields.Int()


class TasksGet(Resource):

    @login_required
    def get(self):
        user = self.g.user
        tasks = Tasks.objects(user=user).order_by('-created_at').all()

        return SerializationSchema().serialize({'items': tasks, 'totals': tasks.count()})
