#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/9 下午2:49

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""

class Solution(object):
    def currect_i(self, nums, i):
        if nums[i] == 0:
            new_nums = [x for x in nums[i:] if x != 0]
            if not new_nums:
                return
            data = nums.pop(i)
            nums.append(data)
            self.currect_i(nums, i)

    def move_zeros(self, nums):
        for i in range(0, len(nums)):
            self.currect_i(nums, i)

        print nums


if __name__ == '__main__':
    solution = Solution()
    solution.move_zeros([0, 0, 12, 9, 0])