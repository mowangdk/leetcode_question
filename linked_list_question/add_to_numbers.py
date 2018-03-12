#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/3/12 下午3:20

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def add_two_numbers(self, l1, l2):
        last_node = last_node_v2 = ListNode(None)
        add_carry = 0
        while (l1 and l2):
            sum = l1.val + l2.val + add_carry
            if sum >= 10:
                sum %= 10
                add_carry = 1
            else:
                add_carry = 0
            current_node = ListNode(sum)
            last_node.next = current_node
            l1 = l1.next
            l2 = l2.next
            last_node = current_node
        while l1 and not l2:
            if add_carry:
                l1.val += 1
                if l1.val >= 10:
                    l1.val %= 10
                    add_carry = 1
                else:
                    add_carry = 0
            last_node.next = l1
            last_node = l1
            l1 = l1.next
        while l2 and not l1:
            if add_carry:
                l2.val += 1
                if l2.val >= 10:
                    l2.val %= 10
                    add_carry = 1
                else:
                    add_carry = 0
            last_node.next = l2
            last_node = l2
            l2 = l2.next
        if add_carry:
            add_carry_node = ListNode(1)
            last_node.next = add_carry_node

        return last_node_v2.next


if __name__ == '__main__':
    # code11 = ListNode(1)
    # code21 = ListNode(2)
    # code31 = ListNode(3)
    # code11.next = code21
    # code21.next = code31
    #
    # code12 = ListNode(4)
    # code22 = ListNode(3)
    # code32 = ListNode(2)
    # code12.next = code22
    # code22.next = code32

    code11 = ListNode(0)
    code12 = ListNode(7)
    code22 = ListNode(3)
    code12.next = code22

    solution = Solution()
    solution.add_two_numbers(code11, code12)
