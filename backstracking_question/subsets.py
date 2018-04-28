#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/28 下午8:01


class Solution(object):
    def subsets(self, nums):
        if nums is None:
            return []
        self.res = []
        self.dfs(0, sorted(nums), [])
        return self.res

    def dfs(self, i, nums, subres):
        if subres:
            self.res.append(subres)
        for j in range(i, len(nums)):
            self.dfs(j + 1, nums, subres + [nums[j]])


if __name__ == '__main__':
    solution = Solution()
    print solution.subsets([1, 2, 3])