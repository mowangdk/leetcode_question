#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/25 上午11:56

import time


# from top to bottom
class Solution(object):
    def cut_rod(self, p, n):
        if n == 0:
            return 0
        max_profit = None
        for i in range(1, n + 1):
            max_profit = max(max_profit, p[i] + self.cut_rod(p, n - i))
        return max_profit


# from top to bottom with cache
class Solution2(object):
    def __init__(self):
        self.max_profit_dict = dict()

    def cut_rod(self, p, n):
        if n in self.max_profit_dict:
            return self.max_profit_dict[n]
        if n == 0:
            return 0
        max_profit = None
        for i in range(1, n + 1):
            max_profit = max(max_profit, p[i] + self.cut_rod(p, n - i))
        self.max_profit_dict[n] = max_profit
        return max_profit


# from bottom to top
class Solution3(object):
    def cut_rod(self, p, n):
        max_value = [0] * (n + 1)
        length_first_value = list(max_value)
        for i in range(1, n + 1):
            max_value_i = 0
            for j in range(1, i + 1):
                if max_value_i < p[j] + max_value[i - j]:
                    max_value_i = p[j] + max_value[i - j]
                    length_first_value[i] = j    # 长度为i的 第一段最优解为j
                max_value_i = max(max_value_i, p[j] + max_value[i - j])
            max_value[i] = max_value_i
        return max_value[n], length_first_value


if __name__ == '__main__':
    p = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20, 9: 24, 10: 30}
    n = 10
    start_time = time.time()
    solution = Solution2()
    print solution.cut_rod(p, n)
    end1 = time.time()
    print 'with cache time', end1 - start_time
    solution1 = Solution()
    solution1.cut_rod(p, n)
    end2 = time.time()
    print 'no cache time', end2 - end1
    solution2 = Solution3()
    max_value, s = solution2.cut_rod(p, n)
    while n > 0:
        print s[n]
        n -=  s[n]
    print 'bottom to top time', time.time() - end2
