#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/6 下午4:55


class Solution(object):

    def remove_duplicates(self, nums):
        if not nums:
            return 0
        j = 0
        for i in xrange(0, len(nums)):
            if nums[i] != nums[j]:
                nums[i], nums[j + 1] = nums[j + 1], nums[i]
                j += 1
        return j + 1


if __name__ == '__main__':
    solution = Solution()
    print solution.remove_duplicates([1, 1, 1, 2, 2, 3, 4, 5])
