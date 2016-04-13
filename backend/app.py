import json
import logging
import os
from wsgiref import simple_server

import falcon
import middlewares
import redis


class Counter(object):
    def __init__(self):
        self.redis = redis.StrictRedis(host=os.getenv('REDIS_HOST', 'redis'), port=6379, db=0)
        if not self.redis.exists('counter'):
            self.redis.set('counter', 0)

    def on_get(self, req, resp):
        req.context['result'] = self.redis.incr('counter')

app = falcon.API(middleware=[
    middlewares.RequireJSON(),
    middlewares.JSONTranslator()
])

app.add_route('/api/counter', Counter())


if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 6000, app)
    httpd.serve_forever()
