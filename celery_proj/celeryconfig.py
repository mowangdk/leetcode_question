#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/3/23 下午8:05


# 直接使用RabbitMQ的缺省用户 guest 以及缺省虚拟主机
BROKER_URL = 'amqp://guest:guest@localhost:5672//'

# Redis同样使用默认数据库 0
CELERY_RESULT_BACKEND = 'redis://10.200.3.16:6379/0'

# 设定导入任务模块路径
CELERY_IMPORTS = ['proj.task.tasks']