#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/3/19 下午10:12
from trees_question.binary_tree_inorder_traversal import TreeNode


class Solution(object):
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(postorder[len(postorder) - 1])
        index = inorder.index(postorder[len(postorder) - 1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index + 1:], postorder[index: len(postorder) - 1])
