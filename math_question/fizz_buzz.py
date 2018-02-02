#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/2/1 下午9:22


class Solution(object):
    def fizz_buzz(self, n):
        new_list = list()
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                new_list.append('FizzBuzz')
            elif i % 3 == 0:
                new_list.append('Fizz')
            elif i % 5 == 0:
                new_list.append('Buzz')
            else:
                new_list.append(str(i))
        return new_list

if __name__ == '__main__':
    solution = Solution()
    print solution.fizz_buzz(15)
