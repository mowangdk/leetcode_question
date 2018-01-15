#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/10 下午8:46
import time


class Solution(object):
    min_length = 9999999
    length_data = list()

    def check_min_data(self, origin_nums):
        current_depth = len(origin_nums)
        last_data = None
        current_length = 0
        self.calculate(origin_nums, current_depth, last_data, current_length)

    def dist(self, x1, x2, last_data):
        if not last_data:
            return 0
        return ((x1 - x2) ** 2 + (last_data[0] - last_data[1]) ** 2) ** 0.5

    def calculate(self, nums, current_depth, last_data, current_length):
        if current_depth == 0:
            self.length_data.append(current_length)
            if current_length < self.min_length:
                self.min_length = current_length
            return
        for location in nums:
            data = self.dist(location[0], location[1], last_data)
            current_length += data
            left_nums = list(nums)
            left_nums.remove(location)
            self.calculate(left_nums, current_depth - 1, location, current_length)

if __name__ == '__main__':
    start_time = time.time()
    solution = Solution()
    nums = [(1, 2), (2, 4), (5, 6), (7, 8), (9, 9), (2, 2), (2, 3), (6, 7), (8, 0), (8, 1), (8, 2)]
    # nums = [(1, 2), (2, 4), (5, 6)]
    solution.check_min_data(nums)
    print solution.min_length
    print len(solution.length_data)
    print time.time() - start_time