#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/12 下午3:53


import time


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(args, kwargs)
        cr.next()
        return cr
    return start


def follow(thefile):
    thefile.seek(0, 2)   # go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def source_follow(thefile, target):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


@coroutine
def sink_follow():
    while True:
        line = (yield)
        print line


def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line


@coroutine
def grep2(pattern, target):
    print 'logging for %s' % pattern
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)


if __name__ == '__main__':
    logfile = open('access-log')
    # logfiles = follow(logfile)
    # pylines = grep('python', logfiles)
    # # pull results out of the processing pipeline
    # for line in pylines:
    #     print line

    # 我们可以将source和sink和filter连接在一起
    source_follow(logfile, grep2('python', sink_follow))

