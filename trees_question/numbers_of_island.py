#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/21 下午8:26


"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        map_count = dict()
        for i in range(len(grid)):
            column_length = len(grid[i])
            for j in range(column_length):
                if int(grid[i][j]) == 1:
                    if i - 1 >= 0 and int(grid[i - 1][j]) == 1:
                        map_count[(i, j)] = (i - 1, j)
                    if j - 1 >= 0 and int(grid[i][j - 1]) == 1:
                        if (i, j) in map_count:
                            map_count[(i, j)] = [(map_count[(i, j)]), (i, j - 1)]
                        else:
                            map_count[(i, j)] = (i, j - 1)
                    if (i, j) not in map_count:
                        map_count[(i, j)] = None
        for key, value in map_count.iteritems():
            if value is None:
                count += 1
            elif isinstance(value, list):
                count -= 1
        return count


if __name__ == '__main__':
    solution = Solution()
    print solution.numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]])
