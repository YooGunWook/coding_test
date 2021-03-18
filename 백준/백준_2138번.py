from itertools import combinations
import copy

n = int(input())
now = list(map(int, input()))
now1 = copy.deepcopy(now)
now2 = copy.deepcopy(now)
end = list(map(int, input()))


def switcher(now, i, n):
    values = [i - 1, i, i + 1]
    for value in values:
        if value < 0:
            continue
        if value >= n:
            continue
        if now[value] == 1:
            now[value] = 0
        elif now[value] == 0:
            now[value] = 1
    return now


def change_zero(now):
    cnt = 0
    for i in range(0, len(now)):
        print(now, 1)
        if i == 0:
            now = switcher(now, i, n)
            cnt += 1
            continue
        if now[i - 1] == end[i - 1]:
            continue
        cnt += 1
        now = switcher(now, i, n)
        print(now, 2)
    if now == end:
        return cnt
    return 10000000000


def change_no_zero(now):
    cnt = 0
    for i in range(1, len(now)):
        if now[i - 1] == end[i - 1]:
            continue
        cnt += 1
        now = switcher(now, i, n)
    if now == end:
        return cnt
    return 10000000000


cnt1 = change_zero(now1)
cnt2 = change_zero(now1)
if cnt1 == cnt2 == 10000000000:
    ans = -1
else:
    ans = min(cnt1, cnt2)
print(ans)
