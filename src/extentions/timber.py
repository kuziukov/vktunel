import logging
import timber

logger = None


def init_timber(app):
    global logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    timber_handler = timber.TimberHandler(
        source_id='23612',
        api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL2FwaS50aW1iZXIuaW8vIiwiZXhwIjpudWxsLCJpYXQiOjE1NjYzODkyNTUsImlzcyI6Imh0dHBzOi8vYXBpLnRpbWJlci5pby9hcGlfa2V5cyIsInByb3ZpZGVyX2NsYWltcyI6eyJhcGlfa2V5X2lkIjo0MDAwLCJ1c2VyX2lkIjoiYXBpX2tleXw0MDAwIn0sInN1YiI6ImFwaV9rZXl8NDAwMCJ9.T859aMMNpJxn6_48_OgNjFGZsub_b2cBySLbM__vFVU'
    )
    logger.addHandler(timber_handler)
    app.logger.addHandler(logger)
    return
