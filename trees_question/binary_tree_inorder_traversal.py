#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/3/13 下午2:45

"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3

return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.data = list()

    def inorder_traversal(self, root):
        if root is None:
            return self.data
        self.inorder_traversal(root.left)
        self.data.append(root.val)
        self.inorder_traversal(root.right)
        return self.data

if __name__ == '__main__':
    solution = Solution()
    solution.inorder_traversal()