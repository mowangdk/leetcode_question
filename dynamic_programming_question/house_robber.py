#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/29 下午8:54


class Solution(object):

    def rob(self, nums):
        if len(nums) > 3:
            rob_max_money = max(nums[0] + self.rob(nums[2:]), nums[1] + self.rob(nums[3:]))
        else:
            if len(nums) == 0:
                rob_max_money = 0
            else:
                rob_max_money = max(nums[0], nums[-1])
        return rob_max_money


class Solution2(object):

    def rob(self, nums):
        now = last = 0
        for i in nums:
            last, now = now, max(i + last, now)
        return now

if __name__ == '__main__':
    solution = Solution()
    print solution.rob([3, 2, 4, 1, 4])
