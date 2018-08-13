#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
"""


class Solution(object):
    def findNumberOfLIS(self, nums):
        dp, longest = [[1, 1] for _ in range(len(nums))], 1
        print dp
        for i in range(1, len(nums)):
            curr_longest, count = 1, 0
            for j in range(i):
                if nums[j] < nums[i]:
                    curr_longest = max(curr_longest, dp[j][0] + 1)
            for j in range(i):
                if dp[j][0] == curr_longest - 1 and nums[j] < nums[i]:
                    count += dp[j][1]
            dp[i] = [curr_longest, max(count, dp[i][1])]
            longest = max(longest, curr_longest)
        return sum([item[1] for item in dp if item[0] == longest])



if __name__ == '__main__':
    solution = Solution()
    solution.findNumberOfLIS([1, 3, 4, 5, 2])
