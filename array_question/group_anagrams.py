#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/2/26 下午8:27


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        all_result = list()
        for i in range(len(strs)):
            sub_list = strs[i+1:]
            answer_result = [strs[i]]
            is_exists = [result for result in all_result if strs[i] in result]
            if not is_exists:
                for j in sub_list:
                    if strs[i] == j or (len(set(strs[i]) ^ set(j)) == 0 and strs[i] and j):
                        answer_result.append(j)
                all_result.append(answer_result)
            else:
                continue
        return all_result


class Solution1(object):
    def groupAnagrams(self, strs):
        temp_dict = {}
        for word in strs:
            word_key = "".join(sorted(word))
            if word_key not in temp_dict:
                temp_dict[word_key] = [word]
            else:
                temp_dict[word_key].append(word)
        print temp_dict
        result = list()
        for value in temp_dict.values():
            result += [value]
        return result


if __name__ == '__main__':
    solution = Solution()
    print solution.groupAnagrams(["tea","and","ace","ad","eat","dans"])
