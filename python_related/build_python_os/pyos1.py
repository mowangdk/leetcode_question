#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/13 下午6:06


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

    def run(self):
        return self.target.send(self.sendval)