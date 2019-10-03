# -*- coding:utf-8 -*-
x = [1, 2, 3, 4, 2, 3, 4, 51, 1, -1, 3, 0]


def max_sub_sequence_sum(sub_sequence):
    res = 0
    i = 0
    while i < len(sub_sequence):
        j = i
        temp_sum = 0
        while j < len(sub_sequence):
            temp_sum += sub_sequence[j]
            if temp_sum > res:
                res = temp_sum
            j += 1
        i += 1
    return res


print max_sub_sequence_sum(x)
