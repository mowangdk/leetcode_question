#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/16 上午10:53


# 系统调用基类, 所有的系统操作需要继承这个类

"""
真实的操作系统有一个强大的"隔离保护"的概念 (内存保护),
应用程序与系统内核之间是松散的，（traps只是一个接口）

我们会通过以下方式模仿真正的操作系统:
     task 对schedule是不可见的
     task 之间是不可见的
     yield 只是一个外部接口
"""


class SystemCall(object):

    def handle(self):
        pass


class GetTid(SystemCall):

    def handle(self):
        self.task.sendval = self.task.tid    # task的sendval 属性其实像一个系统调用的返回值， 这个值被重新发给task,并且使task再次运行
        self.sched.schedule(self.task)


class NewTask(SystemCall):

    def __init__(self, target):
        self.target = target

    def handle(self):
        tid = self.sched.new(self.target)
        self.task.sendval = tid
        self.sched.schedule(self.task)


class KillTask(SystemCall):

    def __init__(self, tid):
        self.tid = tid

    def handle(self):
        task = self.sched.taskmap.get(self.tid, None)
        if task:
            task.target.close()
            self.task.sendval = True
        else:
            self.task.sendval = False
        self.sched.schedule(self.task)


# def foo():
#     mytid = yield GetTid()
#     while True:
#         print "I'm foo", mytid
#         yield
#
#
# def main():
#     child = yield NewTask(foo())
#     for i in xrange(5):
#         yield
#     yield KillTask(child)
#     print "main done"
#
#
# if __name__ == '__main__':
#     sched = Scheduler()
#     sched.new(main())
#     sched.mainloop()
