#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/2/27 下午2:58

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest_str = ""
        exists_list = list()
        for i in range(len(s)):
            if not exists_list or s[i] not in exists_list:
                exists_list.append(s[i])
            else:
                current_str = ''.join(exists_list)
                if len(current_str) > len(longest_str):
                    longest_str = current_str
                index = exists_list.index(s[i])
                exists_list = exists_list[index + 1:] + [s[i]]
        if exists_list:
            current_str = ''.join(exists_list)
            if len(current_str) > len(longest_str):
                longest_str = current_str
        return len(longest_str)


if __name__ == '__main__':
    solution = Solution()
    print solution.lengthOfLongestSubstring("abcabcbb")


