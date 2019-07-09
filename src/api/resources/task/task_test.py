from flask import json
from api.auth.decorators import login_required
from api.resources.task import TaskSchema
from cores.marshmallow_core import ApiSchema
from cores.marshmallow_core import fields
from cores.rest_core import Resource
from pywebpush import webpush, WebPushException
from models.subscription_fcm import FCMSubscription


class SerializationSchema(ApiSchema):

    items = fields.Nested(TaskSchema, many=True)
    totals = fields.Int()


class TasksTest(Resource):

    @login_required
    def post(self):

        data = json.dumps({
            'title': 'Мы скачали ваш альбом',
            'body': 'Привет, мы загрузили ваш альбом, ждем вас най сайте',
        })

        notifications = FCMSubscription.objects(user=self.g.user)
        for notify in notifications:
            try:
                webpush(
                    subscription_info=notify.subscription,
                    data=data,
                    vapid_private_key='7HMkTWy9s8fAI6rH6ZtKCI3i_Wk9hEXDxzEPCoeERdw',
                    vapid_claims={
                        'sub': 'mailto:{}'.format('dsadas@gmail.com'),
                    }
                )
            except WebPushException:
                notify.delete()
        return
