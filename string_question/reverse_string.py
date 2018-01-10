#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/10 下午2:47


class Solution(object):
    def reverse_string(self, s):
        s_length = len(s)
        s = list(s)
        self.reverse(s, 0, s_length)
        return ''.join(s)

    def reverse(self, s, start, end):
        for i in range(start, (start + end) / 2):
            s[i], s[start + end - i - 1] = s[start + end - i - 1], s[i]


class Solution2(object):
    def reverse_string(self, s):
        return s[::-1]


class Solution3(object):
    def reverse_string(self, s):
        if len(s) <= 1:
            return s
        left_s = s[:len(s) / 2]
        right_s = s[len(s) / 2:]
        return self.reverse_string(right_s) + self.reverse_string(left_s)


if __name__ == '__main__':
    solution = Solution3()
    print solution.reverse_string(['a', 'b', 'c', 'd', 'e', 'f'])
