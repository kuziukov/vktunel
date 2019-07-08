from api.auth.decorators import login_required
from api.resources.task import TaskSchema
from marshmallow_core import ApiSchema, fields
from models.tasks import Tasks
from rest_core import Resource


class SerializationSchema(ApiSchema):

    items = fields.Nested(TaskSchema, many=True)
    totals = fields.Int()


class TasksGet(Resource):

    @login_required
    def get(self):
        user = self.g.user
        tasks = Tasks.objects(user=user)

        return SerializationSchema().serialize({'items': tasks, 'totals': tasks.count()})
