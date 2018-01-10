#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/8 下午5:24


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)
        new_nums = nums + nums
        nums = new_nums[nums_length-k: 2 * nums_length-k]
        print nums


class Solution2(object):
    def rotate(self, nums, k):
        nums_length = len(nums)
        k %= nums_length
        self.reverse(nums, 0, nums_length - k)
        self.reverse(nums, nums_length - k, nums_length)
        self.reverse(nums, 0, nums_length)

    def reverse(self, nums, start, end):
        for x in range(start, (start + end) / 2):
            nums[x], nums[start + end - x - 1] = nums[start + end - x - 1], nums[x]
        print nums


if __name__ == '__main__':
    solution = Solution2()
    solution.rotate([1, 2, 3, 4, 5], 1)
