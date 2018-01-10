#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/10 下午4:36


# Time Limit Exceeded
class Solution(object):
    def first_uniq_char(self, s):
        for i in range(len(s)):
            for j in range(0, len(s)):
                if i == j:
                    continue
                data = ord(s[i]) ^ ord(s[j])
                if data == 0:
                    break
            else:
                return i
        return -1


class Solution2(object):
    def first_uniq_char(self, s):
        letters = dict()
        for c in s:
            letters[c] = letters[c] + 1 if c in letters else 1
        for i in range(len(s)):
            if letters[s[i]] == 1:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    print solution.first_uniq_char('cc')