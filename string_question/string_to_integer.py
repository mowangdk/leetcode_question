#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/12 下午8:20


class Solution(object):
    def my_atoi(self, str_data):
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        # checkout none situation & whitespace
        str_data = str_data.strip()
        if not str_data:
            return 0

        flag = 1
        if str_data[0] in ['+', '-']:
            if str_data[0] == '-':
                flag = -1
            str_data = str_data[1:]
        # check "+", "-" situation and the first char is not number
        if not str_data or not str_data[0].isdigit():
            return 0
        # Ignore all char after the first no-number char
        for i, v in enumerate(str_data):
            if not v.isdigit():
                str = str_data[:i]
                break
        result = 0
        for v in str_data[:]:
            result += ord(v) - ord('0')
            result *= 10
        result /= 10
        result *= flag
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        return result


if __name__ == '__main__':
    solution = Solution()
    solution.my_atoi('-11122')
