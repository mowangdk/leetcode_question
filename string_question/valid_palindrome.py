#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/11 下午4:45


class Solution(object):
    def is_palindrome(self, s):
        if s == '':
            return True
        new_s = list()
        for c in s:
            if c.isalnum():
                new_s.append(c.lower())
        for i in range(0, len(new_s) / 2):
            if new_s[len(new_s) - i - 1] != new_s[i]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print solution.is_palindrome('A man, a plan, a canal Panama')
