#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/13 下午6:06
import types

from python_related.build_python_os.system_call import SystemCall


class Task(object):
    """
    Task 包裹在coroutine外部
    只有一个run方法
    run() 执行任务到下一个yield（也就是一个trap）
    """
    taskid = 0

    def __init__(self, target):
        Task.taskid += 1
        self.tid = Task.taskid  # Task ID
        self.target = target    # target coroutine
        self.sendval = None     # value to send
        self.func = target.gi_code.co_name
        self.stack = list()

    def run(self):
        while True:
            try:
                result = self.target.send(self.sendval)
                if isinstance(result, SystemCall): return result
                if isinstance(result, types.GeneratorType):
                    self.stack.append(self.target)
                    self.sendval = None
                    self.target = result
                else:
                    if not self.stack:
                        return
                    self.sendval = result
                    self.target = self.stack.pop()
            except StopIteration:
                if not self.stack:
                    raise
                self.sendval = None
                self.target = self.stack.pop()

