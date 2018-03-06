#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/2/28 下午5:18

class Solution(object):
    def longestPalindrome(self, s):
        palindrome = ""
        for i in range(len(s)):
            first_str = self.get_longest_palindrome(s, i, i)
            len1 = len(first_str)
            if len1 > len(palindrome):
                palindrome = first_str
            second_str = self.get_longest_palindrome(s, i, i + 1)
            len2 = len(second_str)
            if len2 > len(palindrome):
                palindrome = second_str
        return palindrome

    def get_longest_palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

