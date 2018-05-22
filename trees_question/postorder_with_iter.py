#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/5/3 下午5:30


"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

"""


class Solution(object):

    def __init__(self):
        self.stack = list()
        self.result = list()

    def postorderTraversal(self, root):

        """
        :param root:
        :return:
        """
        if root == None:
            return

        myStack1 = list()
        myStack2 = list()

        node = root

        myStack1.append(node)
        while myStack1:
            # 这个while循环的功能是找出后序遍历的逆序， 存储在myStack2里面
            node = myStack1.pop()
            if node.left:
                myStack1.append(node.left)
            if node.right:
                myStack1.append(node.right)
            myStack2.append(node)
        while myStack2:
            self.result.append(myStack2.pop().val)