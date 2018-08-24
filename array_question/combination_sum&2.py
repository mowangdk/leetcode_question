#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def combination_sum(self, candidates, target):
        def DFS(candidates, target, start, valuelist):
            length = len(candidates)
            if target == 0:
                ret.append(valuelist)
                return
            for i in range(start, length):
                if target < candidates[i]:
                    return
                DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])
        candidates.sort()
        ret = []
        DFS(candidates, target, 0, [])
        return ret


class Solution1(object):
    def combination_sum2(self, candidates, target):
        def DFS(candidates, target, start, value_list):
            if target == 0:
                ret.append(value_list)
            length = len(candidates)
            for i in range(start, length):
                if target < candidates[i]:
                    return
                DFS(candidates, target - candidates[i], i + 1, value_list + [candidates[i]])
        candidates.sort()
        ret = []
        DFS(candidates, target, 0, [])
        return ret


if __name__ == '__main__':
    solution = Solution()
    print solution.combination_sum([2, 3, 6, 7], 7)

