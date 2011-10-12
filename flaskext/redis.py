"""Flask integration for Redis"""

import redis as _redis

class Redis(object):
    def __init__(self, app=None):
        if app is not None:
            self.app = app
            self.init_app(app)
        else:
            self.app = None
    
    def init_app(self, app):
        self.app = app
        self.app.config.setdefault(u"REDIS_HOST", u"localhost")
        self.app.config.setdefault(u"REDIS_PORT", 6379)
        self.app.config.setdefault(u"REDIS_DB", 0)
        self.app.config.setdefault(u"REDIS_PASSWORD", None)
        self.redis_instance = _redis.Redis(host=self.app.config[u"REDIS_HOST"],
                                          port=self.app.config[u"REDIS_PORT"],
                                          db=self.app.config[u"REDIS_DB"],
                                          password=self.app.config[u"REDIS_PASSWORD"])

