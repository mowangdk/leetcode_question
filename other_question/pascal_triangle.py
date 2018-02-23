#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/2/23 下午9:29

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        outer_list = list()
        if numRows > 0:
            for i in range(1, numRows + 1):
                if i == 1:
                    outer_list.append([1])
                elif i == 2:
                    outer_list.append([1, 1])
                else:
                    last_inter_list = outer_list[-1]
                    current_inter_list = [1]
                    for j in range(len(last_inter_list)):
                        if j + 1 < len(last_inter_list):
                            current_data = last_inter_list[j] + last_inter_list[j + 1]
                            current_inter_list.append(current_data)
                    current_inter_list.append(1)
                    outer_list.append(current_inter_list)
        return outer_list


if __name__ == '__main__':
    solution = Solution()
    print solution.generate(5)