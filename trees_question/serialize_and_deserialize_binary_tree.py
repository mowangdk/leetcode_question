#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列/反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且这个字符串可以被反序列化得到一个原始的树结构。

示例:

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与LeetCode目前使用的方式一致，详情请参阅 how LeetCode OJ serializes a binary tree。你并非必须采取这种方式，你也可以创造性的用其他的方式解决这个问题。

说明: 不要使用类的成员/全局/静态变量来存储状态机，你的序列化和反序列化算法应该是无状态机的。
"""
from trees_question.KthSmallestElementInBST import TreeNode


# 目前已知这么做有两个风险， 1. 如果将所有val都 str化， 那么负数就会变成了两个字符 "-", "1"
# 2. 当val有重复的时候, 根据前序遍历和中序遍历构建树的过程中， 根据val找index会出现问题。
class Codec:

    def serialize(self, root):
        """
        encodes a tree to a single string
        :param root:
        :return:
        """

        if root is None:
            return ""
        tree_inorder_list = list()
        tree_preorder_list = list()
        stack = list()
        node = root
        while node or stack:
            while node:
                stack.append(node)
                tree_preorder_list.append(node.val)
                node = node.left
            node = stack.pop()
            tree_inorder_list.append(node.val)
            node = node.right
        result = "".join(map(str, tree_inorder_list)) + '_' + "".join(map(str, tree_preorder_list))
        return result

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.

        :param data:
        :return:
        """
        if not data:
            return None

        tree_inorder_list, tree_preorder_list = data.split('_')
        root = self.format_tree(eval(tree_inorder_list), eval(tree_preorder_list))
        return root

    def format_tree(self, tree_inorder_list, tree_preorder_list):
        if not tree_preorder_list:
            return None
        if len(tree_preorder_list) == 1:
            return TreeNode(tree_preorder_list[0])
        root_node = tree_preorder_list[0]
        root = TreeNode(root_node)
        print root_node
        index = tree_inorder_list.index(root_node)
        root.left = self.format_tree(tree_inorder_list[:index], tree_preorder_list[1: index + 1])
        root.right = self.format_tree(tree_inorder_list[index + 1:], tree_preorder_list[index + 1:])
        return root


class Codec2(object):

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        tree_inorder_list = list()
        tree_preorder_list = list()
        stack = list()
        node = root
        while node or stack:
            while node:
                stack.append(node)
                tree_preorder_list.append((id(node), node.val))
                node = node.left
            node = stack.pop()
            tree_inorder_list.append((id(node), node.val))
            node = node.right
        result = str(tree_inorder_list) + '_' + str(tree_preorder_list)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        tree_inorder_list, tree_preorder_list = data.split('_')
        root = self.format_tree(eval(tree_inorder_list), eval(tree_preorder_list))
        return root

    def format_tree(self, tree_inorder_list, tree_preorder_list):
        if not tree_preorder_list:
            return None
        if len(tree_preorder_list) == 1:
            return TreeNode(tree_preorder_list[0][1])
        root_node = tree_preorder_list[0]
        root = TreeNode(root_node[1])
        index = tree_inorder_list.index(root_node)
        root.left = self.format_tree(tree_inorder_list[:index], tree_preorder_list[1: index + 1])
        root.right = self.format_tree(tree_inorder_list[index + 1:], tree_preorder_list[index + 1:])
        return root


if __name__ == '__main__':
    pass
