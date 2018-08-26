#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/21 下午8:08

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.ordered_list = list()

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.get_ordered_list(root)
        return self.ordered_list[:k]

    def get_ordered_list(self, root):
        self.get_ordered_list(root.left)
        self.ordered_list.append(root.val)
        self.get_ordered_list(root.right)


if __name__ == '__main__':
    solution = Solution()
    solution.kthSmallest()
