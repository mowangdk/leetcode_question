#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/13 下午6:11

from Queue import Queue
from python_related.build_python_os.pyos1 import Task


class Scheduler(object):

    def __init__(self):
        self.ready = Queue()
        self.taskmap = dict()

    def new(self, target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def schedule(self, task):
        self.ready.put(task)

    def mainloop(self):
        while self.taskmap:
            task = self.ready.get()
            result = task.run()
            self.schedule(task)
