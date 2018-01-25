#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/24 下午3:08


class Solution(object):
    def max_profit(self, prices):
        if not prices:
            return 0
        min_buy_price = prices[0]
        max_profit = [0] * len(prices)
        for i in range(1, len(prices)):
            max_profit[i] = max(max_profit[i - 1], prices[i] - min_buy_price)
            min_buy_price = min(min_buy_price, prices[i])
        return max_profit[-1]


if __name__ == '__main__':
    solution = Solution()
    solution.max_profit([7, 6, 4, 3, 1, 9])
