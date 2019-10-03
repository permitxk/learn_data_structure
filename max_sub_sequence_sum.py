# -*- coding:utf-8 -*-
x = [1, 2, 3, 4, 2, 3, 4, 51, 1, -1, 3, 0]


def max_sub_sequence_sum(sub_sequence):
    res = 0
    i = 0
    j = 1
    while i <= len(sub_sequence):
        while j <= len(sub_sequence):
            temp = sub_sequence[i:j]
            temp_sum = sum(temp)
            if temp_sum > res:
                res = temp_sum
                j += 1
            else:
                i = j + 1
                j += 2
    return res


print max_sub_sequence_sum(x)
