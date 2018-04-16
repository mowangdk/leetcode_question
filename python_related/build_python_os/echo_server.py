#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/16 下午6:15

from socket import socket, AF_INET, SOCK_STREAM

from python_related.build_python_os.pyos2 import Scheduler
from python_related.build_python_os.system_call import NewTask, ReadWait, WriteWait

"""
在真正的操作系统里面， 直到IO操作结束， python解释器会一直停止

显然这对我们的多任务操作系统是绝对不可取的（任何的阻塞操作都将冻结整个程序）
"""


# 客户端处理方法， 每个客户端都需要执行这个task
def handle_client(client, addr):
    print "Connection from", addr
    while True:
        yield ReadWait(client)
        data = client.recv(65535)
        if not data:
            break
        yield WriteWait(client)
        client.send(data)
    client.close()
    print "Client close"
    yield    # make the function a generator/coroutine


def server(port):
    print "Server starting"
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(("", port))
    sock.listen(5)  # 同时连接server的数量
    # server loop， 等待新连接， 对每个新的客户端都分配一个新的task去处理
    while True:
        yield ReadWait(sock)
        client, addr = sock.accept()
        yield NewTask(handle_client(client, addr))

# 我们可以看到， io操作阻塞了整个进程

if __name__ == '__main__':
    def alive():
        while True:
            print "I'm alive"
            yield
    sched = Scheduler()
    sched.new(alive())
    sched.new(server(45000))
    sched.mainloop()
