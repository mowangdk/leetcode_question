# -*- coding: utf-8 -*-

import collections
import functools
import select
import time


class IOLoop(object):
    _EPOLLIN = 0x001
    _EPOLLOUT = 0x004
    _EPOLLERR = 0x008
    _EPOLLHUP = 0x010

    READ = _EPOLLIN
    WRITE = _EPOLLOUT
    ERROR = _EPOLLERR | _EPOLLHUP

    PULL_TIMEOUT = 1

    def __init__(self):
        self.handlers = {}
        self.events = {}
        self.epoll = select.epoll()

        self._future_callbacks = collections.deque()

    def initialize(self, make_current=None):
        if make_current is None:
            if IOLoop.current(instance=False) is None:
                self.make_current()
        elif make_current:
            current = IOLoop.current(instance=False)
            if current is not None and current is not self:
                raise RuntimeError("current IOLoop already exists")
            self.make_current()

    def make_current(self):
        old = getattr(IOLoop, '_instance', None)
        if old is not None:
            old.clear_current()
        IOLoop._instance = self

    @staticmethod
    def clear_current():
        old = IOLoop.current(instance=False)
        if old is not None:
            old._clear_current_hook()
        IOLoop._instance = None

    def _clear_current_hook(self):
        """
        子类继承实现，作为回收当前实例的hook
        :return:
        """
        pass

    @staticmethod
    def instance():
        """
        Deprecated alias for `IOLoop.current()`.

        :return:
        """
        return IOLoop.current()

    @staticmethod
    def current(instance=True):
        """
        instance == True ，when current is None generate new IOLoop instance，
        Returns the current thread's `IOLoop`
        :return:
        """
        current = getattr(IOLoop, '_instance', None)
        if not current and instance:
            IOLoop._instance = IOLoop()
        return IOLoop._instance

    def add_handler(self, fd_obj, handler, event):
        fd = fd_obj.fileno()
        self.handlers[fd] = (fd_obj, handler)
        self.epoll.register(fd, event)

    def update_handler(self, fd, event):
        self.epoll.modify(fd, event)

    def remove_handler(self, fd):
        self.handlers.pop(fd, None)
        try:
            self.epoll.unregister(fd)
        except Exception as error:
            print 'epoll unregister failed %r' % error

    def replace_handler(self, fd, handler):
        self.handlers[fd] = (self.handlers[fd][0], handler)

    def start(self):
        try:
            while True:
                for i in xrange(len(self._future_callbacks)):
                    callback = self._future_callbacks.popleft()
                    callback()
                events = self.epoll.poll(self.PULL_TIMEOUT)
                self.events.update(events)
                while self.events:
                    fd, event = self.events.popitem()
                    try:
                        fd_obj, handler = self.handlers[fd]
                        handler(fd_obj, event)
                    except Exception as error:
                        print 'ioloop callback error: %r' % error
                        time.sleep(0.5)
        finally:
            for fd, _ in self.handlers.items():
                self.remove_handler(fd)
            self.epoll.close()

    # def run_sync(self, func, timeout=None):
    #     """
    #     start the `IOLoop`, runs the given function, and stop the loop
    #
    #     The function must return either a yieldable object or
    #     ``None``. If the function returns a yieldable object, the
    #     `IOLoop` will run until the yieldable is resolved (and
    #     `run_sync()` will return the yieldable's result). If it raises
    #     an exception, the `IOLoop` will stop and the exception will be
    #     re-raised to the caller.
    #
    #     ```
    #     @gen.coroutine
    #     def main():
    #         # do stuff
    #
    #     if __name__ == '__main__':
    #         IOLoop.current().run_sync(main)
    #     ```
    #
    #     :param func:
    #     :param timeout:
    #     :return:
    #     """
    #     future_cell = [None]
    #
    #     def run():
    #         try:
    #             result = func()
    #             if result is not None:
    #                 from tornado.gen import convert_yielded
    #                 result = convert_yielded(result)
    #         except Exception:
    #             future_cell[0] = Future()
    #             future_set_exc_info(future_cell[0], sys.exc_info())
    #         else:
    #             if is_future(result):
    #                 future_cell[0] = result
    #             else:
    #                 future_cell[0] = Future()
    #                 future_cell[0].set_result(result)
    #         self.add_future(future_cell[0], lambda future: self.stop())
    #     self.add_callback(run)
    #     if timeout is not None:
    #         def timeout_callback():
    #             if not future_cell[0].cancel():
    #                 self.stop()
    #         timeout_handle = self.add_timeout(self.time() + timeout, timeout_callback)
    #     self.start()
    #     if timeout is not None:
    #         self.remove_timeout(timeout_handle)
    #     if future_cell[0].canncelled() or not future_cell[0].done():
    #         raise TimeoutError('Operation time out after %s seconds' % timeout)
    #     return future_cell[0].result(0)

    def add_future_callback(self, callback, *args, **kwargs):
        self._future_callbacks.append(
            functools.partial(callback, *args, **kwargs)
        )

    def add_future(self, future, callback):
        future.add_done_callback(
            lambda future: self.add_future_callback(callback, future)
        )

