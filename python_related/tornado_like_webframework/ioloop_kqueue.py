# encoding: utf-8

"""
kevent filters

KQ_FILTER_READ	Takes a descriptor and returns whenever there is data available to read
KQ_FILTER_WRITE	Takes a descriptor and returns whenever there is data available to write
KQ_FILTER_AIO	AIO requests
KQ_FILTER_VNODE	Returns when one or more of the requested events watched in fflag occurs
KQ_FILTER_PROC	Watch for events on a process id
KQ_FILTER_NETDEV	Watch for events on a network device [not available on Mac OS X]
KQ_FILTER_SIGNAL	Returns whenever the watched signal is delivered to the process
KQ_FILTER_TIMER	Establishes an arbitrary timer

kevent flags

KQ_EV_ADD	Adds or modifies an event
KQ_EV_DELETE	Removes an event from the queue
KQ_EV_ENABLE	Permitscontrol() to returns the event
KQ_EV_DISABLE	Disablesevent
KQ_EV_ONESHOT	Removes event after first occurrence
KQ_EV_CLEAR	Reset the state after an event is retrieved
KQ_EV_SYSFLAGS	internal event
KQ_EV_FLAG1	internal event
KQ_EV_EOF	Filter specific EOF condition
KQ_EV_ERROR	See return values

"""

import select


_EPOLLIN = 0x001
_EPOLLOUT = 0x004
_EPOLLERR = 0x008
_EPOLLHUP = 0x010

READ = _EPOLLIN
WRITE = _EPOLLOUT
ERROR = _EPOLLERR | _EPOLLHUP

PULL_TIMEOUT = 1


class _KQueue(object):
    """A kqueue-based event loop for BSD/Mac systems"""

    def __init__(self):
        self._kqueue = select.kqueue()
        self._active = {}

    def fileno(self):
        self._kqueue.fileno()

    def close(self):
        self._kqueue.close()

    def modify(self, fd, events):
        self.unregister(fd)
        self.register(fd, events)

    def register(self, fd, events):
        if fd in self._active:
            raise IOError("fd %s already registered" % fd)
        self._control(fd, events, select.KQ_EV_ADD)
        self._active[fd] = events

    def unregister(self, fd):
        events = self._active.pop(fd)
        self._control(fd, events, select.KQ_EV_DELETE)

    def _control(self, fd, events, flags):

        kevents = list()

        if events & WRITE:
            kevents.append(select.kevent(fd, filter=select.KQ_FILTER_WRITE, flags=flags))

        if events & READ:
            kevents.append(select.kevent(fd, filter=select.KQ_FILTER_READ, flags=flags))

        for kevent in kevents:
            self._kqueue.control([kevent], 0)

    def poll(self, timeout):
        kevents = self._kqueue.control(None, 1000, timeout)
        events = {}
        for kevent in kevents:
            fd = kevent.ident
            if kevent.filter == select.KQ_FILTER_READ:
                events[fd] = events.get(fd, 0) | READ

            if kevent.filter == select.KQ_FILTER_WRITE:
                if kevent.flags & select.KQ_EV_EOF:
                    events[fd] = ERROR
                else:
                    events[fd] = events.get(fd, 0) | ERROR
            if kevent.flags & select.KQ_EV_ERROR:
                events[fd] = events.get(fd, 0) | ERROR
        return events.items()

