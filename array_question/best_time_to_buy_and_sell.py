#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/6 下午6:05


class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

if __name__ == '__main__':
    solution = Solution()
    solution.maxProfit([1, 2, 4, 5, 2, 1])
