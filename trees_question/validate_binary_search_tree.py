#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/19 下午3:16


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        def inorder_traversal(root):
            if root:
                inorder_traversal(root.left)
                inorder.append(root)
                inorder_traversal(root.right)

        inorder = list()
        if not root:
            return True
        inorder_traversal(root)
        if sorted(inorder) == inorder:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    root = None
    solution.isValidBST(root)
