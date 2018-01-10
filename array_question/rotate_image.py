#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/9 下午7:54


class Solution(object):
    def rotate_image(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix


class Solution2(object):
    def rotate_image(self, matrix):
        new_matrix = zip(*matrix)
        print matrix
        for i in new_matrix:
            list(i).reverse()
        return new_matrix


if __name__ == '__main__':
    solution = Solution2()
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print solution.rotate_image(matrix)