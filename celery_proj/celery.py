#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/3/23 下午8:05
# 该模块能够自动被celery cmd识别， 并自动加载模块中的app对象， 以此来启动worker service


from celery_proj.app_factory import make_app

app = make_app()
