#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from collections import deque


class Solution(object):
    def merge(self, p_list, p_start, p_mid, p_end):

        lnums = p_list[p_start: p_mid + 1]
        rnums = p_list[p_mid + 1: p_end + 1]
        lnums.append(sys.maxint)
        rnums.append(sys.maxint)
        l = r = 0
        for i in range(p_start, p_end + 1):
            if lnums[l] < rnums[r]:
                p_list[i] = lnums[l]
                l += 1
            else:
                p_list[i] = rnums[r]
                r += 1

    def merge_sort(self, p_list, p_start, p_end):

        if p_start < p_end:
            mid = (p_start + p_end) >> 1
            self.merge_sort(p_list, p_start, mid)
            self.merge_sort(p_list, mid + 1, p_end)
            self.merge(p_list, p_start, mid, p_end)


class Solution2(object):

    def merge_sort(self, lst):
        if len(lst) <= 1:
            return lst

        def merge(left, right):
            merged, left, right = deque(), deque(left), deque(right)
            while left and right:
                merged.append(left.popleft() if left[0] < right[0] else right.popleft())
            merged.extend(right if right else left)
            return merged
        middle = int(len(lst) // 2)
        left = self.merge_sort(list[:middle])
        right = self.merge_sort(list[middle:])
        return merge(left, right)




if __name__ == '__main__':
    nums = [10, 8, 4, -1, 2, 6, 7, 3]
    print 'num is:', nums
    merge_sort(nums, 0, 7)
    print 'merge sort:', nums
