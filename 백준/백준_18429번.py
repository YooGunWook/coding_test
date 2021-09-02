from itertools import permutations

n, k = list(map(int, input().split(" ")))
weight = list(map(int, input().split(" ")))


def solution(weight):
    count = 0
    for obj in permutations(weight, n):
        muscle = 500
        tmp_muscle = []
        for inc in obj:
            muscle = muscle + inc - k
            if muscle < 500:
                break
            tmp_muscle.append(muscle)
        if len(tmp_muscle) == n:
            count += 1
    return count


print(solution(weight))
