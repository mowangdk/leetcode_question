#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/18 下午5:57


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        new_list = list()
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                new_list.append(l1.val)
                l1 = l1.next
            else:
                new_list.append(l2.val)
                l2 = l2.next
        while l1 is not None:
            new_list.append(l1)
            l1 = l1.next
        while l2 is not None:
            new_list.append(l2)
            l2 = l2.next
        return new_list


if __name__ == '__main__':
    solution = Solution()
    solution.mergeTwoLists([1, 2, 3], [2, 3, 5])
