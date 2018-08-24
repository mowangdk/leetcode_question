#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

"""


class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = n + 2
        for i in range(n):
            if abs(nums[i]) <= n:
                curr = abs(nums[i]) - 1
                nums[curr] = -abs(nums[curr])

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


class Solution1(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1


if __name__ == '__main__':
    pass
