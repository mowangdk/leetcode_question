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

    def dist(self, current_data, last_data):
        if not last_data:
            return 0
        return ((current_data[0] - last_data[0]) ** 2 + (current_data[1] - last_data[1]) ** 2) ** 0.5

    def calculate(self, nums, current_depth, last_data, current_length):
        if current_depth == 0:
            current_length += self.dist(self.first_data, last_data)
            self.length_data.append(current_length)
            if current_length < self.min_length:
                self.min_length = current_length
            return
        for location in nums:
            if last_data is None:
                current_length = 0
                self.first_data = location
            data = self.dist(location, last_data)
            new_length = data + current_length
            left_nums = list(nums)
            left_nums.remove(location)
            self.calculate(left_nums, current_depth - 1, location, new_length)


def distance_count(list_points):
    solution = Solution()
    current_length = 0
    for i in range(1, len(list_points)):
        current_length += solution.dist(list_points[i], list_points[i - 1])

    print current_length

if __name__ == '__main__':
    start_time = time.time()
    solution = Solution()
    nums = [(6, 9), (5, 6), (3, 1), (1, 4), (1, 8), (4, 3), (2, 4), (3, 5)]
    # nums = [(1, 2), (2, 4), (5, 6)]
    solution.check_min_data(nums)
    print solution.min_length
    # print solution.length_data
    # distance_count([(9, 8), (4, 4), (3, 9), (4, 9), (9, 9), (9, 8)])

