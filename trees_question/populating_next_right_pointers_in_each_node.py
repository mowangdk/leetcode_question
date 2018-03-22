#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/3/20 下午4:42


"""
 Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

    You may only use constant extra space.
    You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

For example,
Given the following perfect binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

"""


class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self._next = None


class Solution(object):
    def __init__(self):
        self.levels = list()

    def connect(self, root):
        if root is not None:
            return root
        root._next = None
        self.connect_right([root])
        for level in self.levels:
            for i in reversed(range(len(level))):
                if i == len(level) - 1:
                    level[i]._next = None
                else:
                    level[i]._next = level[i + 1]

    def connect_right(self, last_top_level):
        rest = []
        if not last_top_level:
            return None
        for last_level_node in last_top_level:
            if last_level_node.left is not None:
                rest.append(last_top_level.left)
            if last_level_node.right is not None:
                rest.append(last_top_level.right)
        if not rest:
            return None

        self.levels.append(rest)
        self.connect_right(rest)


if __name__ == '__main__':
    pass
