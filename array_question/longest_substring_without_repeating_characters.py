#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/2/27 下午2:58


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


