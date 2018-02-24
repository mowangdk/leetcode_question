#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/2/24 上午10:41


class Solution(object):
    def isValid(self, a):
        pars = [None]
        parmap = {')': '(', "}": "{", "]": "["}
        for c in a:
            if c in parmap and parmap[c] == pars[len(pars) - 1]:
                pars.pop()
            else:
                pars.append(c)
        return len(pars) == 1


if __name__ == '__main__':
    solution = Solution()
    print solution.isValid("")
