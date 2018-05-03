#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/27 下午8:23


"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            for j in self.permute(nums[:i] + nums[i + 1:]):
                res.append([nums[i]] + j)
        return res

if __name__ == '__main__':
    solution = Solution()
    print solution.permute([1, 2, 3])