#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/17 下午9:00


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverse_link(self, head):
        if not head:
            return []
        new_node = ListNode(0)
        new_node.next = head
        head_next = head.next
        while head_next:
            head.next = head_next.next
            head_next.next = new_node.next
            new_node.next = head_next
            head_next = head.next
        return new_node.next


class Solution2(object):
    def reverse_link(self, head):
        if not head or not head.next:
            return head
        p = head.next
        n = self.reverse_link(p)
        head.next = None
        p.next = head
        return n


if __name__ == '__main__':
    solution = Solution()
    solution.reverse_link(0)