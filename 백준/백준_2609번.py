import copy

v1, v2 = list(map(int, input().split(" ")))


def solution(v1, v2):
    tmp_v1 = copy.deepcopy(v1)
    tmp_v2 = copy.deepcopy(v2)
    while tmp_v1 % tmp_v2 != 0:
        v3 = tmp_v1 % tmp_v2
        tmp_v1 = tmp_v2
        tmp_v2 = v3
    return tmp_v2


gcd = solution(v1, v2)
print(gcd)
print((v1 * v2) // gcd)
