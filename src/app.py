from flask import Flask
from extentions import (
    init_cors,
    init_logging
)


def create_app():
    app = Flask(__name__, static_folder=None, static_url_path=None)
    app.config.from_object('config')
    init__blueprints(app)
    init_extentions(app)
    return app


def init_extentions(app):
    init_cors(app=app)
    #init_logging(app=app)


def init__blueprints(app):
    from web.routes import web_bp
    app.register_blueprint(web_bp)


if __name__ == '__main__':
    create_app().run(host='0.0.0.0')
