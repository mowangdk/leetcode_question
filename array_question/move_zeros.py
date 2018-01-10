#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/9 下午2:49


class Solution(object):
    def currect_i(self, nums, i):
        if nums[i] == 0:
            new_nums = [x for x in nums[i:] if x != 0]
            if not new_nums:
                return
            data = nums.pop(i)
            nums.append(data)
            self.currect_i(nums, i)

    def move_zeros(self, nums):
        for i in range(0, len(nums)):
            self.currect_i(nums, i)

        print nums


if __name__ == '__main__':
    solution = Solution()
    solution.move_zeros([0, 0, 12, 9, 0])