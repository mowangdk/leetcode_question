#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/6 下午4:55

"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.

"""


class Solution(object):
    def remove_duplicates(self, nums):
        if not nums:
            return 0
        j = 0
        for i in xrange(0, len(nums)):
            if nums[i] != nums[j]:
                nums[i], nums[j + 1] = nums[j + 1], nums[i]
                j += 1
        return j + 1


if __name__ == '__main__':
    solution = Solution()
    print solution.remove_duplicates([1, 1, 1, 2, 2, 3, 4, 5])
