#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/2/6 下午10:30


class Solution(object):
    def euclid(self, a, b):
        if b == 0:
            return a
        return self.euclid(b, a % b)

if __name__ == '__main__':
    solution = Solution()
    print solution.euclid(3, 5)
