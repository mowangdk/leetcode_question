#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/23 下午7:56


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p = m - 1
        q = n - 1
        new_tail = m + n - 1
        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                nums1[new_tail] = nums1[p]
                p -= 1
                new_tail -= 1
            else:
                nums_data = nums2[q]
                nums1[new_tail] = nums_data
                q -= 1
                new_tail -= 1
        nums1[:q+1] = nums2[:q+1]
        print nums1


class Solution2(object):
    def merge(self, nums1, m, nums2, n):
        p, q = m - 1, n - 1
        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                nums1[p + q + 1] = nums1[p]
                p -= 1
            else:
                nums1[p+q+1] = nums2[q]
                q -= 1
        nums1[:q+1] = nums2[:q+1]


if __name__ == '__main__':
    solution = Solution()
    solution.merge([1, 2, 6, 7, None, None, None], 4, [4, 5, 6], 3)