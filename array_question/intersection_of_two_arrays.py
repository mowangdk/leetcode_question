#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/9 上午11:35

"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:

    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""

import collections


class Solution(object):
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        p1 = p2 = 0
        ans = list()
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                ans.append(nums1[p1])
                p1 += 1
                p2 += 1
        return ans


class Solution2(object):
    def intersection(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        c = collections.Counter(nums1)
        ans = list()
        for x in nums2:
            if c[x] > 0:
                ans += x,
                c[x] -= 1
        return ans

if __name__ == '__main__':
    solution = Solution2()
    ans = solution.intersection([1, 2, 2, 3], [1, 2, 2])
    print ans
