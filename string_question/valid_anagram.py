#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/10 下午5:42


class Solution(object):
    def valid_anagram(self, s, t):
        list_s = list(s)
        list_t = list(t)
        if len(list_s) != len(list_t):
            return False
        list_s.sort()
        list_t.sort()
        for i in range(len(list_s)):
            if list_s[i] != list_t[i]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    s = ''
    t = ''
    print solution.valid_anagram(s, t)