#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/16 下午9:11


def add(x, y):
    yield x + y


def main():
    r = yield add(2, 2)
    print r
    yield


def run():
    m = main()
    sub = m.send(None)
    result = sub.send(None)
    m.send(result)


if __name__ == '__main__':
    run()