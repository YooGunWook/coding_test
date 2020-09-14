import collections


def solution(clothes):
    answer = 1
    case = collections.Counter(x[1] for x in clothes).values()
    for c in case:
        answer *= c + 1
    return answer - 1

