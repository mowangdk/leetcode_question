#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/3/23 下午8:04

# 这里使用absolute_import 是因为proj包中的celery模块与celery库重名了， 所以需要指明celery从绝对路径中导入
from __future__ import absolute_import
from celery import Celery


def make_app():
    app = Celery('celery_proj')
    # a module named celeryconfig.py must be available to load from the current directory or on the Python path.
    app.config_from_object('celery_proj.celeryconfig')
    return app
