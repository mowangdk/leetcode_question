#!/usr/bin/env python
# -*- coding: utf-8 -*-


def foo(n):
    return [range(i, i + n) for i in range(1, n * n, n)]


def foo2(n):
    return [[n * i + j for j in range(1, n + 1)] for i in range(n)]


if __name__ == '__main__':
    print foo2(5)
    print foo(4)

