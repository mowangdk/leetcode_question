#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/18 下午7:40


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 快慢指针法找链表的中点, 使用另一个栈存储
class Solution(object):
    def isPalindrome(self, head):
        fast = slow = head
        new_list = list()
        while fast and fast.next is None:
            new_list.insert(0, slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        for val in new_list:
            if val != slow.val:
                return False
            slow = slow.next
        return True


# in-place change
class Solution2(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.fast
        slow = self.reverseList(slow)
        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True

    def reverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head


if __name__ == '__main__':
    pass

