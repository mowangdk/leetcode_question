#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/26 下午9:16


"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left - 1, right):
                    yield q
                for q in generate(p + ')', left, right - 1):
                    yield q
        return list(generate('', n, n))


class Solution1(object):
    def deep(self, tot, ln, rn, strs, lis):
        if ln < tot:
            self.deep(tot, ln + 1, rn, strs + '(', lis)
        if rn < ln <= tot:
            self.deep(tot, ln, rn + 1, strs + ')', lis)
        if ln == tot and rn == tot:
            lis.append(strs)

    def generateParenthesis(self, n):
        """
        :param n:
        :return:
        """

        lis = list()
        self.deep(n, 0, 0, '', lis)
        return lis


class Solution2(object):
    def generateParenthesis(self, n):
        """
        :param n:
        :return:
        """
        def genrate(p, left, right, parens=list()):
            if left:
                genrate(p + '(', left - 1, right)
            if right < left:
                genrate(p + ')', left, right - 1)
            if not right:
                parens += p
            return parens
        return genrate("", n, n)


if __name__ == '__main__':
    solution = Solution()
    solution.generateParenthesis(3)