#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def get_next(self, origin_str, next_list):
        str_length = len(origin_str)
        next_list[0] = -1
        k = -1
        j = 0
        while j < str_length - 1:
            if k == -1 or origin_str[j] == origin_str[k]:
                k += 1
                j += 1
                next_list[j] = k
            else:
                k = next_list[k]

    def kmp_search(self, origin_str, parten, next_list):
        i = 0
        j = 0
        s_len = len(origin_str)
        p_len = len(parten)
        while i < s_len and j < p_len:
            if j == -1 or origin_str[i] == origin_str[j]:
                j += 1
                i += 1
            else:
                j = next_list[j]
        if j == p_len:
            return i - j
        else:
            return -1


if __name__ == '__main__':
    solution = Solution()
