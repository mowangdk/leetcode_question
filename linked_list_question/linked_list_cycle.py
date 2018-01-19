#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/18 下午9:06


class Solution(object):
    def hasCycle(self, head):
        fast = slow = head
        while fast.next is not None or fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    solution.hasCycle(0)