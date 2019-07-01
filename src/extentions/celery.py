from celery import Celery

celery = None


def init_celery(app):
    global celery
    celery = Celery(__name__)
    celery.config_from_object(app.config['CELERY_SETTINGS'])
    return


def download_album(user_id, community_id, album_id, task_id):
    task = celery.send_task(
        'download-album',
        args=[user_id, community_id, album_id, task_id]
    )
    return task
