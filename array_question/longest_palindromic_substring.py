#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/2/28 下午5:18


class Solution(object):
    def longestPalindrome(self, s):
        palindrome = ""
        for i in range(len(s)):
            len1 = len(self.get_longest_palindrome(s, i, i))
            if len1 > len(palindrome):
                palindrome = self.get_longest_palindrome(s, i, i)
            len2 = len(self.get_longest_palindrome(s, i, i + 1))
            if len2 > len(palindrome):
                palindrome = self.get_longest_palindrome(s, i, i + 1)
        return palindrome

    def get_longest_palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

