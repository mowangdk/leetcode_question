#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/25 下午9:33


class Solution(object):

    def __init__(self):
        self.digits_map = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                           '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                           '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits):
        def dfs(num, string, res):
            if num == length:
                res.append(string)
                return
            for letter in self.digits_map[digits[num]]:
                dfs(num + 1, string + letter, res)

        res = []
        length = len(digits)
        dfs(0, '', res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.letterCombinations(['2', '3'])
    pass