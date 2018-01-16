#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/16 上午11:06


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype str
        """
        min_length_str = min(strs, key=lambda x: len(x))
        str_list_export_min = [str_data for str_data in strs if min_length_str != str_data]
        common_list = list()
        for i in range(len(min_length_str)):
            for j in str_list_export_min:
                if j[i] == min_length_str[i]:
                    continue
                else:
                    return "".join(common_list)
            else:
                common_list.append(min_length_str[i])
        return "".join(common_list)


if __name__ == '__main__':
    solution = Solution()
    print solution.longestCommonPrefix(["longest", "l"])

