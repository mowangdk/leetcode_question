#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/9 下午2:24

"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution(object):
    def plus_one(self, nums):
        add_carry = 0
        for i in reversed(range(0, len(nums))):
            new_num = nums[i] + 1
            if new_num >= 10:
                new_num %= 10
                nums[i] = new_num
                add_carry = 1
                continue
            else:
                add_carry = 0
                nums[i] = new_num
                break
        if add_carry:
            nums.insert(0, add_carry)
        return nums

if __name__ == '__main__':
    solution = Solution()
    print solution.plus_one([9])