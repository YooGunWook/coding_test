# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections


def solution(A, K):
    if not A:
        return A
    A = collections.deque(A)
    for _ in range(K):
        tmp = A.pop()
        A.appendleft(tmp)
    return list(A)


print(solution([3, 8], 3))
