# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import collections


def solution(A):
    value_dict = collections.Counter(A)
    for i in value_dict:
        if value_dict[i] % 2 != 0:
            return i


print(solution([9, 3, 9, 3, 9, 7, 9]))
