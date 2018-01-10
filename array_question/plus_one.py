#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/9 下午2:24


class Solution(object):
    def plus_one(self, nums):
        add_carry = 0
        for i in reversed(range(0, len(nums))):
            new_num = nums[i] + 1
            if new_num >= 10:
                new_num %= 10
                nums[i] = new_num
                add_carry = 1
                continue
            else:
                add_carry = 0
                nums[i] = new_num
                break
        if add_carry:
            nums.insert(0, add_carry)
        return nums

if __name__ == '__main__':
    solution = Solution()
    print solution.plus_one([9])