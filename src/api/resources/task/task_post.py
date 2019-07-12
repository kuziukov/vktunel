from flask import g
from api.auth.decorators import login_required
from api.resources.task import TaskSchema
from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields
from cores.vk import API
from extentions.celery import download_album
from models.notification import Notification, NotificationsData
from models.tasks import Tasks
from cores.rest_core import Resource


class SerializationSchema(ApiSchema):

    task = fields.Nested(TaskSchema)
    taskId = fields.Str(default=None)


class TasksPost(Resource):

    @login_required
    def get(self, community_id, album_id):
        user = g.user
        api = API(user.access_token, v=5.95)
        response = api.photos.getAlbums(owner_id=f'-{community_id}', need_covers=1, album_ids=album_id)
        albums = response['items'][0]

        tasks = Tasks()
        tasks.community_id = community_id
        tasks.album_id = album_id
        tasks.user = g.user
        tasks.album_name = dict(albums).get('title')
        tasks.save()

        notification = Notification()
        notification.user = g.user
        notification.type = 'TaskAdded'
        notification.parent = NotificationsData()
        notification.parent.task = tasks
        notification.save()

        res = download_album(user_id=str(g.user.id), community_id=community_id, album_id=album_id,
                             task_id=str(tasks.id))

        response = {
            'task': tasks,
            'taskId': res
        }

        return SerializationSchema().serialize(response)
