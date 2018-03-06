#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/9 上午10:52

"""

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""

class Solution(object):
    def single_number(self, nums):
        first_number = nums[0]
        for i in range(1, len(nums)):
            first_number = nums[i] ^ first_number
        print first_number

if __name__ == '__main__':
    solution = Solution()
    solution.single_number([1, 1, 2, 2, 3, 3, 4, 5])