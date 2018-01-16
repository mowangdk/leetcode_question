#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/15 下午4:48


class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return -1
        needle_length = len(needle)
        for index in range(len(haystack) - len(needle) + 1):
            if haystack[index] == needle[0]:
                if haystack[index: index + needle_length] == needle:
                    return index
        return -1


if __name__ == '__main__':
    solution = Solution()
    haystack, needle = "hello", "ll"
    print solution.strStr(haystack, needle)
