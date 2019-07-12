from marshmallow import EXCLUDE
from marshmallow.validate import Range
from api.auth.decorators import login_required
from api.resources.task import TaskSchema
from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields
from models.tasks import Tasks
from cores.rest_core import Resource


class FiltersSchema(ApiSchema):

    start = fields.Int(default=None, missing=0, validate=Range(min=0))
    limit = fields.Int(default=None, missing=50, validate=Range(min=0))
    start_time = fields.Timestamp(default=None)
    end_time = fields.Timestamp(default=None)


class SerializationSchema(ApiSchema):

    items = fields.Nested(TaskSchema, many=True)
    totals = fields.Int()


class TasksGet(Resource):

    @login_required
    def get(self):
        user = self.g.user
        filters = FiltersSchema().deserialize(self.request.args, unknown=EXCLUDE)

        query_kwargs = {}

        if 'start_time' in filters:
            query_kwargs['created_at__gte'] = filters['start_time']

        if 'end_time' in filters:
            query_kwargs['created_at__lte'] = filters['end_time']

        tasks = Tasks.objects(user=user).filter(**query_kwargs)
        items = tasks.skip(filters['start']).limit(filters['limit'])

        return SerializationSchema().serialize({'items': items, 'totals': items.count()})
