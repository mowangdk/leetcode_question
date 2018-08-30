# -*- coding: utf-8 -*-
# @Time  :  2018/1/8 下午5:24


class Solution(object):
    def dynamic_basic(self, container_weight, object_weights, object_values):
        weight_values = zip(object_weights, object_values)
        weight_values.sort(key=lambda x: x[0])
        print weight_values
        init_values = [[-1 for j in range(container_weight + 1)] for i in range(len(weight_values) + 1)]
        # 初始化第0行
        for index, i in enumerate(init_values):
            i[0] = 0
            if index == 0:
                for j in range(len(i)):
                    i[j] = 0

        for i in range(1, len(weight_values) + 1):
            current_weight, current_value = weight_values[i - 1]
            for j in range(1, container_weight + 1):

                if current_weight > j:
                    init_values[i][j] = init_values[i - 1][j]
                else:
                    new_value = init_values[i - 1][j - current_weight] + current_value
                    old_value = init_values[i - 1][j]
                    init_values[i][j] = max(new_value, old_value)
        print init_values


if __name__ == '__main__':
    container_weight = 10
    object_weights = [2, 2, 6, 5, 4]
    object_values = [6, 3, 5, 4, 6]
    solution = Solution()
    solution.dynamic_basic(container_weight, object_weights, object_values)
