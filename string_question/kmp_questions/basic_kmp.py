#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def get_next(self, pattern_str):
        str_length = len(pattern_str)
        next_list = [-1] * str_length
        k = -1
        j = 0
        # 这里 P[k] 表示前缀， P[j] 表示后缀
        while j < str_length - 1:
            if k == -1 or pattern_str[j] == pattern_str[k]:
                k += 1
                j += 1
                next_list[j] = k
            else:
                k = next_list[k]
        return next_list

    # 为了防止 p[j] == p[next[j]] 的情况，导致重复匹配。我们对getNext方法优化如下

    def get_better_next(self, pattern_str):
        p_str_len = len(pattern_str)
        next_list = [-1] * p_str_len
        k = -1
        j = 0
        while j < p_str_len - 1:
            if k == -1 or pattern_str[j] == pattern_str[k]:
                j += 1
                k += 1
                if pattern_str[j] != pattern_str[k]:
                    next_list[j] = k
                else:
                    # 因为不能出现 p[j] = p[ next[j]], 所以当出现时需要继续递归， k = next[k] = next[next[k]]
                    next_list[j] = next_list[k]
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
    # print solution.get_next('DABCDABDE')
    print solution.get_next('ABCDABD')
