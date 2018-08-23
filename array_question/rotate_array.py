#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/8 下午5:24

"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

"""


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
