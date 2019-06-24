from flask_redis import FlaskRedis

session_store = None


def init_redis(app):
    global session_store
    session_store = FlaskRedis(config_prefix='SESSION_STORE')
    session_store.init_app(app=app)
    return

