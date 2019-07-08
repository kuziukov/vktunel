from flask import render_template, redirect, url_for, g
from models.tasks import Tasks
from extentions.celery import download_album
from vk import API
from utils import convert_size
from models.notification import Notification, NotificationsData
from api.auth.decorators import web_login_required


@web_login_required
def task_page():
    tasks = Tasks.objects(user=g.user).order_by('-created_at').all()
    return render_template('task_page.html', tasks=tasks, convert_size=convert_size)


@web_login_required
def task_post(community_id, album_id):

    api = API(g.user.access_token, v=5.95)
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

    res = download_album(user_id=str(g.user.id), community_id=community_id, album_id=album_id, task_id=str(tasks.id))

    return redirect(url_for('web.albums', community_id=community_id))
