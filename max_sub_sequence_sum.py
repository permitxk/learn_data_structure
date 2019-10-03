# -*- coding:utf-8 -*-
# x = '-2 11 -4 13 -5 -2'
x = raw_input()
x = x.split(' ')
x = [float(i) for i in x]


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

# 在线处理


def better_max_sub_sequence_sum(sub_sequence):
    now_list = max_list = 0
    for k in range(len(sub_sequence)):
        now_list += sub_sequence[k]
        if now_list > max_list:
            max_list = now_list
        elif now_list < 0:
            now_list = 0
    return max_list


print better_max_sub_sequence_sum(x)
