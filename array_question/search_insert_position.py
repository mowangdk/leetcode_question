#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left


if __name__ == '__main__':
    solution = Solution()
    solution .searchInsert([1, 3, 5, 6], 4)
