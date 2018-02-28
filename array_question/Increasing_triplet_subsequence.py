#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/2/28 下午8:27

import bisect

class Solution(object):
    def increasingTriplet(self, nums):
        self.LTS = [nums[0]]
        for i in range(1, len(nums)):
            num = nums[i]
            if num > self.LTS[-1]:
                self.LTS.append(nums)
            else:
                index = bisect.bisect_left()


if __name__ == '__main__':
    pass