#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/5/3 下午5:30


class Solution(object):

    def isSymmetric(self, root):
        if not root:
            return True
        return self.mirror(root.left, root.right)

    def mirror(self, left, right):
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        return self.mirror(left.left, right.right) and self.mirror(left.right, right.left)


class Solution2(object):

    def isSymmetric(self, root):
        if not root:
            return True

        stackl, stackr = [root.left], [root.right]
        while len(stackl) > 0 and len(stackr) > 0:
            left_node = stackl.pop(0)
            right_node = stackr.pop(0)
            if not left_node and not right_node:
                continue
            elif not left_node or not right_node:
                return False
            if left_node.val != right_node.val:
                return False
            stackl.append(left_node.left)
            stackl.append(left_node.right)
            stackr.append(right_node.right)
            stackr.append(right_node.left)
        return len(stackl) == 0 and len(stackr) == 0


if __name__ == '__main__':
    solution = Solution()
    root = None
    print solution.isSymmetric(root)
