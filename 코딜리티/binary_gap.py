# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import re


def solution(N):
    value = bin(N)[2:]
    max_len = 0
    count = 0
    if "0" not in value or "1" not in value:
        return max_len
    for i in value:
        if i == "1":
            if max_len < count:
                max_len = count
            count = 0
        else:
            count += 1
    return max_len


print(solution(20))