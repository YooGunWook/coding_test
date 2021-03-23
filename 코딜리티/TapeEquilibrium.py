import collections


def solution(A):
    min_val = 10000000
    sum_a = sum(A)
    for i in range(len(A) - 1):
        A[i + 1] = A[i] + A[i + 1]
        min_val = min(abs(sum_a - A[i] - A[i]), min_val)
    return min_val


print(solution([3, 1]))
