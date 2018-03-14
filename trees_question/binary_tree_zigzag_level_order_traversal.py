#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/3/13 下午3:16

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

Python

"""


class Solution(object):
    def __init__(self):
        self.result = []

    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        else:
            root_level = [root]
            self.result.append(root_level)
            self.level_search(root_level)
        for i in xrange(len(self.result)):
            if i % 2 == 1:
                self.result[i].reverse()
            self.result[i] = [each.val for each in self.result[i]]
        return self.result

    def level_search(self, up_level_nodes):
        ret = list()
        if len(up_level_nodes) == 0:
            self.result.pop()
            return
        for each_node in up_level_nodes:
            if each_node.left is not None:
                ret.append(each_node.left)
            if each_node.right is not None:
                ret.append(each_node.right)
        if len(ret) == 0:
            return
        self.result.append(ret)
        self.level_search(ret)


if __name__ == '__main__':
    solution = Solution()
    solution.zigzagLevelOrder()
