from api.auth.decorators import login_required
from models.tasks import Tasks
from cores.rest_core import Resource
from celery.result import AsyncResult
from extentions.celery import celery


class TasksStatusGet(Resource):

    def get(self, task_id):
        #user = self.g.user

        res = AsyncResult(task_id, app=celery)

        print(res.state)

        print(task_id)

        return
