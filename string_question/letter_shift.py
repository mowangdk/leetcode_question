#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
有一个由小写字母组成的字符串 S，和一个整数数组 shifts。

我们将字母表中的下一个字母称为原字母的 移位（由于字母表是环绕的， 'z' 将会变成 'a'）。

例如·，shift('a') = 'b'， shift('t') = 'u',， 以及 shift('z') = 'a'。

对于每个 shifts[i] = x ， 我们会将 S 中的前 i+1 个字母移位 x 次。

返回将所有这些移位都应用到 S 后最终得到的字符串。

示例：

输入：S = "abc", shifts = [3,5,9]
输出："rpl"
解释：
我们以 "abc" 开始。
将 S 中的第 1 个字母移位 3 次后，我们得到 "dbc"。
再将 S 中的前 2 个字母移位 5 次后，我们得到 "igc"。
最后将 S 中的这 3 个字母移位 9 次后，我们得到答案 "rpl"。
提示：

1 <= S.length = shifts.length <= 20000
0 <= shifts[i] <= 10 ^ 9

"""

import string


class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """

        if len(S) != len(shifts):
            return False
        all_texts = string.ascii_lowercase + string.ascii_lowercase
        list_s = ''
        total_sum = sum(shifts)
        shift_sum = list()
        # 原本是在下面的迭代里面用sum来计算和的， 但是这样时间复杂度就变成了O(n2), 超时。抽出之后正常
        for i in range(len(S)):
            if i != 0:
                total_sum -= shifts[i - 1]
            shift_sum.append(total_sum)

        for i in range(len(S)):
            origin_str = S[i]
            shift_bits = shift_sum[i]
            shift_bits %= 26
            list_s += all_texts[all_texts.index(origin_str) + shift_bits]
        return list_s


if __name__ == '__main__':
    Solution()
