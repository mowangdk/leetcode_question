#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/9 上午10:52


class Solution(object):
    def single_number(self, nums):
        first_number = nums[0]
        for i in range(1, len(nums)):
            first_number = nums[i] ^ first_number
        print first_number

if __name__ == '__main__':
    solution = Solution()
    solution.single_number([1, 1, 2, 2, 3, 3, 4, 5])