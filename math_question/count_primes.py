#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/2/2 上午11:20


class Solution(object):
    def count_primes(self, n):
        if n < 3:
            return 0
        digits = [1] * n
        digits[0] = digits[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if digits[i] == 1:
                for j in range(i+i, n, i):
                    digits[j] = 0
        return sum(digits)


if __name__ == '__main__':
    solution = Solution()
    print solution.count_primes(20)
