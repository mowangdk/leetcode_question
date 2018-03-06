#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/9 下午4:43


class Solution(object):
    def two_sum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    solution = Solution()
    target = 10
    print solution.two_sum([2, 5, 5, 11], target)