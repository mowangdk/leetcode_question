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


# return a task's id number
class GetTid(SystemCall):

    def handle(self):
        self.task.sendval = self.task.tid    # task的sendval 属性其实像一个系统调用的返回值， 这个值被重新发给task,并且使task再次运行
        self.sched.schedule(self.task)


# Create a new task
class NewTask(SystemCall):

    def __init__(self, target):
        self.target = target

    def handle(self):
        tid = self.sched.new(self.target)
        self.task.sendval = tid
        self.sched.schedule(self.task)


# kill a task
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


# wait for a task to exit
class WaitTask(SystemCall):

    def __init__(self, tid):
        self.tid = tid

    # WaitTask handler 使得main方法从ready队列出队，进入到exit_waiting 队列中
    def handle(self):
        result = self.sched.waitforexit(self.task, self.tid)
        self.task.sendval = result

        if not result:
            self.sched.schedule(self.task)


# 这两个类只是等待I/O 事件， 但不实际上执行任何I/O
class ReadWait(SystemCall):

    def __init__(self, f):
        self.f = f

    def handle(self):
        fd = self.f.fileno()
        self.sched.wait_for_read(self.task, fd)


class WriteWait(SystemCall):

    def __init__(self, f):
        self.f = f

    def handle(self):
        fd = self.f.fileno()
        self.sched.wait_for_write(self.task, fd)
