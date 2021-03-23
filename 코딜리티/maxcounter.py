# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import collections


def solution(N, A):
    res = [0] * N
    max_val = 0
    A = collections.deque(A)
    while A:
        value = A.popleft()
        if value == N + 1:
            res = [max_val] * N
            continue
        res[value - 1] += 1
        if max_val < res[value - 1]:
            max_val = res[value - 1]
    return res


def solution(N, A):

    counters = N * [0]
    next_max_counter = max_counter = 0

    for oper in A:
        if oper <= N:
            current_counter = counters[oper - 1] = max(
                counters[oper - 1] + 1, max_counter + 1
            )
            next_max_counter = max(current_counter, next_max_counter)
        else:
            max_counter = next_max_counter

    return [c if c > max_counter else max_counter for c in counters]


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
