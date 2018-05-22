#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/5/3 下午5:30


"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""


class Solution(object):
    def __init__(self):
        self.stack = list()
        self.result = list()

    def inorderTraversal(self, root):
        if not root:
            return []
        self.stack.insert(0, root)
        while self.stack:
            while root.left:
                self.stack.insert(0, root.left)
                root = root.left
            root = self.stack.pop(0)
            if root.val == 5:
                print [i.val for i in self.stack]
            self.result.append(root.val)
            while root.right:
                self.stack.insert(0, root.right)
                root = root.right
        return self.result


class Solution2(object):
    def __init__(self):
        self.stack = list()
        self.result = list()

    def inorderTraversal(self, root):
        if root is None:
            return []

        node = root
        while node or self.stack:
            while node:
                self.stack.insert(0, node)
                node = node.left
            node = self.stack.pop()
            self.result.append(node.val)
            node = node.right

