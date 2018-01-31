#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/30 下午8:41


class Solution(object):

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        # reset array to its original configuration and return it
        return self.nums

    def shuffle(self):
        # return a random shuffling of the array
        pass

    def permutations(self, iterable, r=None):
        pool = tuple(iterable)
        n = len(pool)
        r = n if r is None else r
        if r > n:
            return
        indices = range(n)
        cycles = range(n, n - r, -1)
        yield tuple(pool[i] for i in indices[:r])
        while n:
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i + 1:] + indices[i: i + 1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    yield tuple(pool[i] for i in indices[:r])
                    break
            else:
                return


