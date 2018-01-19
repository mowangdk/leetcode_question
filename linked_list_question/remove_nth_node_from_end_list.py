#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/17 下午8:17


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next_ = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        list_node = ListNode(0)
        list_node.next_ = head
        before_head = after_head = list_node
        for _ in range(n):
            after_head = after_head.next_
        while after_head:
            after_head = after_head.next_
            before_head = before_head.next_
        before_head.next_ = before_head.next_.next_
        return before_head.next_


class Solution2(object):
    def removeNthFromEnd(self, head, n):
        def getIndex(head):
            if not head:
                return 0
            index = getIndex(head.next_) + 1
            if index > n:
                head.next_.val = head.val
            return index
        getIndex(head)
        return head.next_


if __name__ == '__main__':
    solution = Solution()
    solution.removeNthFromEnd()