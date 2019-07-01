from flask import make_response
from mongoengine import DoesNotExist, ValidationError
from werkzeug.exceptions import NotFound
from models.tasks import Tasks


def file_download(task_id):
    try:
        task = Tasks.objects(id=task_id).first()
    except (DoesNotExist, ValidationError):
        raise NotFound()

    if task.archive is None:
        raise NotFound()

    filename = 'archive.zip'
    try:
        response = make_response(task.archive.read())
        response.headers['Content-Type'] = task.archive.content_type
        response.headers["Content-Disposition"] = f'attachment; filename={filename}'
    except Exception:
        raise NotFound()

    return response





