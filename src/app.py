from flask import Flask


def create_app():
    app = Flask(__name__, static_folder=None, static_url_path=None)
    app.config.from_object('config')
    init__blueprints(app)
    init_extentions(app)
    return app


def init_extentions(app):
    pass


def init__blueprints(app):
    pass


if __name__ == '__main__':
    create_app().run(host='0.0.0.0')