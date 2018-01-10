#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/10 下午3:35


class Solution(object):
    def reverse_integer(self, s):
        sign = [-1, 1][s > 0]
        str_s = str(abs(s))
        int_str_s = int(str(str_s[::-1]))
        int_str_s *= sign
        minus_range = -2 ** 31
        max_range = 2 ** 31 - 1
        if minus_range < int_str_s < max_range:
            return int_str_s
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
    print solution.reverse_integer(-1563847412)
