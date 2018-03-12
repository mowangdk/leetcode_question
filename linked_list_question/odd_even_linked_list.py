#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/3/12 下午4:28


"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

Credits:
Special thanks to @DjangoUnchained for adding this problem and creating all test cases.

"""


class Solution(object):
    def oddEvenList(self, head):
        if head is None:
            return head
        odd = odd_head = head
        even = even_head = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return odd_head


if __name__ == '__main__':
    solution = Solution()
    solution.oddEvenList()