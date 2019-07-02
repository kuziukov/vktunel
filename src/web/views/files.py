from flask import make_response, Response, stream_with_context
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

    headers = {
        'Content-Type': task.archive.content_type,
        'Content-Disposition': f'attachment; filename={filename}'
    }

    def generate():
        for obj in task.archive.read():
            yield obj

    return Response(stream_with_context(generate()), headers=headers, direct_passthrough=True)





