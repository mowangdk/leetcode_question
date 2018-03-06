#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/2/26 下午8:17

"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.
Follow up:

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""


class Solution(object):
    def setZeroes(self, matrix):
        zero_row_column = set()
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == 0:
                    zero_row_column.add((row, column))

        for row, column in zero_row_column:
            matrix[row] = len(matrix[row]) * [0]
            for row in range(len(matrix)):
                matrix[row][column] = 0

if __name__ == '__main__':
    solution = Solution()
    solution.setZeroes([[1, 2, 3], [2, 0, 4], [4, 0, 5]])
