#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/24 下午1:18


class Solution(object):
    def climb_stairs(self, n):
        if n == 1 or n == 0 or n == 2:
            return n
        temps = [1, 1]
        i = 2
        while i <= n:
            temps.append(temps[i - 1] + temps[i - 2])
            i += 1
        return temps[n]


if __name__ == '__main__':
    solution = Solution()
    n = 8
    solution.climb_stairs(n)
