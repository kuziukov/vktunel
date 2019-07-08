from flask import Flask
from extentions import (
    init_cors,
    init_mongo,
    init_redis,
    init_celery
)


def create_app():
    app = Flask(__name__, static_folder='static_folder', static_url_path=None)
    app.config.from_object('config')
    init_extentions(app)
    init__blueprints(app)
    return app


def init_extentions(app):
    init_cors(app=app)
    init_mongo(app=app)
    init_redis(app=app)
    init_celery(app=app)


def init__blueprints(app):
    from web.routes import web_bp
    from api.routes import api_bp
    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp)


if __name__ == '__main__':
    create_app().run(host='0.0.0.0')
