#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/3/23 下午8:52


from celery_proj.celery import app

@app.task
def add(x, y):
    return x + y