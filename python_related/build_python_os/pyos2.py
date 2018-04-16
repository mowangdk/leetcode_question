#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/13 下午6:11

from Queue import Queue

import select

from python_related.build_python_os.pyos1 import Task
from python_related.build_python_os.system_call import SystemCall, GetTid, NewTask, KillTask

"""
在真实的操作系统里面， 应用程序需要使用traps调用操作系统
"""


class Scheduler(object):

    def __init__(self):
        self.ready = Queue()    # 准备就绪的任务的队列
        self.taskmap = dict()    # 一个dict， 保存并追踪所有的活跃的任务， 每一个task都有一个uniq_id

        # 这是一个所有等待退出的tasks的等待集合，
        self.exit_waiting = dict()

        # 保留所有的阻塞io， 这些字典是由文件描述符映射到任务
        self.read_waiting = dict()
        self.write_waiting = dict()

    def new(self, target):        # 推送一个新的task到队列中
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def exit(self, task):
        print "Task %d terminated" % task.tid
        del self.taskmap[task.tid]
        # 通知其他task等待当前task退出, 其他task进行入队操作
        for task in self.exit_waiting.pop(task.tid, []):
            self.schedule(task)

    def waitforexit(self, task, waittid):
        if waittid in self.taskmap:
            self.exit_waiting.setdefault(waittid, []).append(task)
            return True
        else:
            return False

    # select 模块可以用来监视socket集合（或者file）的活动情况
    # io轮询， 用select判断哪个文件描述符可以被使用， 没有block任意一个关联的任务
    # 比较困难的是我们应该讲iopoll 放在什么位置， 你可以把它放到ioloop中， 但是这有可能导致过度轮询
    # 特别是还有许多 待执行的task在准备队列中的时候
    def iopoll(self, timeout):
        if self.read_waiting or self.write_waiting:
            # r 是传入数据用的sockets的列表
            # w 是准备好接收传出数据的套接字列表
            # e 是错误状态sockets的列表
            r, w, e = select.select(self.read_waiting, self.write_waiting, [], timeout)
            for fd in r:
                self.schedule(self.read_waiting.pop(fd))
            for fd in w:
                self.schedule(self.write_waiting.pop(fd))

    def iotask(self):
        while True:
            if self.ready.empty():
                self.iopoll(None)
            else:
                self.iopoll(0)
            yield

    # 简单的放任务
    def wait_for_read(self, task, fd):
        self.read_waiting[fd] = task

    def wait_for_write(self, task, fd):
        self.write_waiting[fd] = task

    def schedule(self, task):
        self.ready.put(task)    # 将任务推送到ready 队列， 使得任务可以被执行

    def mainloop(self):    # 主调度循环， 它将所有队列中的任务全部执行到yield处
        self.new(self.iotask())
        while self.taskmap:
            task = self.ready.get()
            try:
                result = task.run()
                if isinstance(result, SystemCall):    # 这里注意一下task返回的结果， 如果这个结果是一个系统调用，那么接下来就做一些准备工作之后，以一个任务的方式执行系统调用
                    result.task = task    # 这两个属性主要目的是保存当前程序运行环境信息
                    result.sched = self
                    result.handle()
                    continue
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)


def foo():
    mytid = yield GetTid()
    for i in xrange(5):
        print "I'm foo", mytid
        yield


def bar():
    mytid = yield GetTid()
    for i in xrange(10):
        print "I'm bar", mytid
        yield


def foo_v2():
    mytid = yield GetTid()
    while True:
        print "I'm foo", mytid
        yield


def main():
    child = yield NewTask(foo_v2())
    for i in xrange(5):
        yield
    yield KillTask(child)
    print "main done"


# 每一个任务会跑到yield处
# 在yield的地方， schedule 会重新获取控制权，去切换到其他任务
if __name__ == '__main__':
    # sched = Scheduler()
    # sched.new(foo())
    # sched.new(bar())
    # sched.mainloop()

    sched = Scheduler()
    sched.new(main())
    sched.mainloop()


