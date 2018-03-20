#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/3/14 下午10:08
from trees_question.binary_tree_inorder_traversal import TreeNode


class Solution(object):
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: root_index + 1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
        return root
