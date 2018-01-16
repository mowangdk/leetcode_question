#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/15 下午6:14


class Solution(object):
    def count_and_say(self, n):
        if n == 1:
            return "1"
        else:
            result = self.count_and_say(n - 1)
            same_count = 1
            new_result = list()
            for index in range(0, len(result)):
                if index - 1 >= 0:
                    if result[index] == result[index - 1]:
                        same_count += 1
                    else:
                        new_result.append(str(same_count))
                        new_result.append(str(result[index - 1]))
                        same_count = 1
                if len(result) - 1 == index:
                    new_result.append(str(same_count))
                    new_result.append(result[index])
            return ''.join(new_result)


if __name__ == '__main__':
    solution = Solution()
    n = 6
    result = solution.count_and_say(n)
    print result
