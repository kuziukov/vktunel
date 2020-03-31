import datetime
from datetime import date
from flask import g
from mongoengine import Q
from api.auth.decorators import login_required, valid_subscription
from api.resources.task import TaskSchema
from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields
from cores.vk import API
from extentions.celery import download_album
from models.notification import (
    Notification,
    NotificationsData
)
from models.tasks import Tasks
from cores.rest_core import (
    Resource,
    APIException,
    codes
)
from utils import (
    get_first_day,
    get_last_day
)


class DeserializationSchema(ApiSchema):

    subject_id = fields.Str(required=True)
    album_id = fields.Str(required=True)


class SerializationSchema(ApiSchema):

    task = fields.Nested(TaskSchema)
    taskId = fields.Str(default=None)


class SubjectIdException(APIException):

    @property
    def message(self):
        return 'Subject id exception, please try again later'

    code = codes.BAD_REQUEST


class AlbumsException(APIException):

    @property
    def message(self):
        return 'Albums exception, please try again later'

    code = codes.BAD_REQUEST


class AccountPlanException(APIException):

    @property
    def message(self):
        return 'Your account plan does not allow you to download anymore'

    code = codes.NOT_ALLOWED


def check_account_plan(user):
    currentMonth = date.today()
    firstDayOfMonth = get_first_day(currentMonth)
    lastDayOfMonth = get_last_day(currentMonth)

    countOfTasks = Tasks.objects(user=user).filter(
        Q(created_at__gte=firstDayOfMonth) & Q(created_at__lte=lastDayOfMonth)
    ).count()

    return False if countOfTasks >= user.subscription.plan.limits.numberOfAlbums else True


class TaskPost(Resource):

    @valid_subscription
    def post(self):
        user = g.user
        data = DeserializationSchema().deserialize(self.request.json)

        try:
            if not check_account_plan(user):
                raise AccountPlanException()
        except Exception:
            raise AccountPlanException()

        subject_id = data['subject_id']
        album_id = data['album_id']

        api = API(user.access_token, v=5.95)

        try:
            response = api.photos.getAlbums(owner_id=subject_id, need_covers=1, album_ids=album_id)
        except Exception:
            raise AlbumsException()

        albums = response['items'][0]

        tasks = Tasks()
        tasks.community_id = str(subject_id)
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

        res = download_album(user_id=str(g.user.id), community_id=subject_id, album_id=album_id,
                             task_id=str(tasks.id))

        response = {
            'task': tasks,
            'taskId': res
        }

        return SerializationSchema().serialize(response)
