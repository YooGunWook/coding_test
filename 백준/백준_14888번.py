import collections
from itertools import permutations
import copy

n = int(input())
values = input().split()
oper = list(map(int, input().split(" ")))


def solution(oper, values):
    op = []
    res = []

    for i, k in enumerate(oper):
        if k == 0:
            continue
        if i == 0:
            add = ["+"] * k
            op += add
            continue
        if i == 1:
            minus = ["-"] * k
            op += minus
            continue
        if i == 2:
            mul = ["*"] * k
            op += mul
            continue
        if i == 3:
            div = ["//"] * k
            op += div
            continue

    for ope in set(permutations(op)):
        tmp_ope = collections.deque(list(ope))
        tmp_values = copy.deepcopy(collections.deque(values))
        while tmp_values:
            if len(tmp_values) == 1:
                break
            tmp = ""
            value_1 = tmp_values.popleft()
            tmp += value_1
            ops = tmp_ope.popleft()
            tmp += ops
            value_2 = tmp_values.popleft()
            tmp += value_2
            
            if ops == "//":
                if abs(int(value_1)) < abs(int(value_2)):
                    tmp_values.appendleft(str(0))
                    continue
                if '-' in value_1:
                    value_1 = value_1.replace('-','')
                    tmp_values.appendleft('-'+str(eval(value_1+ops+value_2)))        
                    continue
            tmp_values.appendleft(str(eval(tmp)))

        if int(tmp_values[0]) in res:
            continue
        res.append(int(tmp_values[0]))

    return set(res)


res = solution(oper, values)
print(max(res))
print(min(res))