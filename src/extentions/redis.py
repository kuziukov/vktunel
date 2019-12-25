from flask_redis import FlaskRedis

session_store = None
notification_store = None


def init_redis(app):
    global session_store
    global notification_store
    session_store = FlaskRedis(config_prefix='SESSION_STORE')
    notification_store = FlaskRedis(config_prefix='NOTIFICATION_STORE')
    session_store.init_app(app=app)
    notification_store.init_app(app=app)
    return

