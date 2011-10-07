"""Flask integration for Redis"""

from __future__ import absolute_import
import redis


def init_redis(app):
    """Initializes Redis client from app config"""

    app.config.setdefault('REDIS_HOST', 'localhost')
    app.config.setdefault('REDIS_PORT', 6379)
    app.config.setdefault('REDIS_DB', 0)
    app.config.setdefault('REDIS_PASSWORD', None)

    return redis.Redis(host=app.config['REDIS_HOST'],
                       port=app.config['REDIS_PORT'],
                       db=app.config['REDIS_DB'],
                       password=app.config['REDIS_PASSWORD'])
