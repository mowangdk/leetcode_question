#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/17 上午11:58

from python_related.build_python_os.system_call import ReadWait, WriteWait


def Accept(sock):
    yield ReadWait(sock)
    yield sock.accept()


def Send(sock, buffer):
    while buffer:
        yield WriteWait(sock)
        len = sock.send(buffer)
        buffer = buffer[len:]


def Recv(sock, maxbytes):
    yield ReadWait(sock)
    yield sock.recv(maxbytes)


class Socket(object):
    def __init__(self, sock):
        self.sock = sock

    def accept(self):
        yield ReadWait(self.sock)
        client, addr = self.sock.accept()
        yield Socket(client), addr

    def send(self, buffer):
        while buffer:
            yield WriteWait(self.sock)
            len = self.sock.send(buffer)
            buffer = buffer[len:]

    def recv(self, maxbytes):
        yield ReadWait(self.sock)
        yield self.sock.recv(maxbytes)

    def close(self):
        yield self.sock.close()
