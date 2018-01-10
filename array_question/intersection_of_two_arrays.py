#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/9 上午11:35
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
