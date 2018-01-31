#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/31 上午10:52
import time


class Solution(object):
    def lcs(self, s1, s2):
        if not s1 or not s2:
            return 0
        if s1[0] == s2[0]:
            return 1 + self.lcs(s1[1:], s2[1:])
        else:
            return max(self.lcs(s1[1:], s2), self.lcs(s1, s2[1:]))


class Solution2(object):
    def __init__(self):
        self.tuple_cache = dict()

    def lcs(self, s1, s2):
        tuple_s1 = tuple(s1)
        tuple_s2 = tuple(s2)
        if (tuple_s1, tuple_s2) in self.tuple_cache:
            return self.tuple_cache[(tuple_s1, tuple_s2)]
        if not s1 or not s2:
            self.tuple_cache[(tuple_s1, tuple_s2)] = 0
            return 0
        if s1[0] == s2[0]:
            s1_s2 = 1 + self.lcs(s1[1:], s2[1:])
            self.tuple_cache[(tuple_s1, tuple_s2)] = s1_s2
            return s1_s2
        else:
            s1_s2 = max(self.lcs(s1[1:], s2), self.lcs(s1, s2[1:]))
            self.tuple_cache[(tuple_s1, tuple_s2)] = s1_s2
            return s1_s2


class Solution3(object):
    def lcs(self, s1, s2):
        s1_length = len(s1)
        s2_length = len(s2)
        print s1_length, s2_length
        cost_list = [[0] * (s1_length + 1) for _ in range(s2_length + 1)]
        for i in range(s2_length):
            for j in range(s1_length):
                if s2[i] == s1[j]:
                    cost_list[i][j] = 1 + cost_list[i - 1][j - 1]
                else:
                    cost_list[i][j] = max(cost_list[i - 1][j], cost_list[i][j - 1])
        return cost_list[-1][-1]


if __name__ == '__main__':
    # solution = Solution()
    s1 = "BDCABAHSIJSOJ"
    s2 = "ABCBDABJOSIAHSIJDJSO"
    start_time = time.time()
    # print solution.lcs(s1, s2)
    middle_time = time.time()
    print middle_time - start_time
    solution2 = Solution2()
    print solution2.lcs(s1, s2)
    end_time = time.time()
    print end_time - middle_time
    solution3 = Solution3()
    print solution3.lcs(s1, s2)
    print time.time() - end_time
