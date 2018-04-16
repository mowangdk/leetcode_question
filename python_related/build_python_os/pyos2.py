#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/13 下午6:11

from Queue import Queue
from python_related.build_python_os.pyos1 import Task
from python_related.build_python_os.system_call import SystemCall, GetTid

"""
在真实的操作系统里面， 应用程序需要使用traps调用操作系统
"""


class Scheduler(object):

    def __init__(self):
        self.ready = Queue()    # 准备就绪的任务的队列
        self.taskmap = dict()    # 一个dict， 保存并追踪所有的活跃的任务， 每一个task都有一个uniq_id

    def new(self, target):        # 推送一个新的task到队列中
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def exit(self, task):
        print "Task %d terminated" % task.tid
        del self.taskmap[task.tid]

    def schedule(self, task):
        self.ready.put(task)    # 将任务推送到ready 队列， 使得任务可以被执行

    def mainloop(self):    # 主调度循环， 它将所有队列中的任务全部执行到yield处
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


# 每一个任务会跑到yield处
# 在yield的地方， schedule 会重新获取控制权，去切换到其他任务
if __name__ == '__main__':
    sched = Scheduler()
    sched.new(foo())
    sched.new(bar())
    sched.mainloop()

