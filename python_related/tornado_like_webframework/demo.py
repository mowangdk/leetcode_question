# -*- coding: utf-8 -*-

from python_related.tornado_like_webframework.concurrent import coroutine, Return
from python_related.tornado_like_webframework.fake_tornado import BaseHandler, Application, run_server
import pdb

class AppHandler(BaseHandler):
    @classmethod
    def get(cls, **kwargs):
        pdb.set_trace()
        return "Marry Christmas"


class AsyncHandler(BaseHandler):
    @classmethod
    @coroutine
    def yield_something(cls):
        raise Return("value from yield")


    @classmethod
    @coroutine
    def get(cls, *args, **kwargs):
        result = yield cls.yield_something()
        raise Return(result)


if __name__ == '__main__':
    app = Application([('/app', AppHandler), ('/\d+', AppHandler), ('/s', AsyncHandler)])
    run_server('0.0.0.0', 8080, application=app)
