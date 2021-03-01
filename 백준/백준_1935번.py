import collections

n = int(input())
lists = collections.deque(list(input()))
operator = ["*", "+", "-", "/"]
nums = collections.defaultdict(int)
tmp = []
for i in lists:
    if i not in operator:
        tmp.append(i)
tmp = list(set(tmp))
tmp.sort()
for i in tmp:
    nums[i] = float(input())


def solution(lists):
    tmp = []
    while lists:
        value = lists.popleft()
        if value not in operator:
            tmp.append(nums[value])
            continue

        if value in operator:
            ev = ""
            vl1 = tmp.pop()
            vl2 = tmp.pop()
            ev = str(vl2) + value + str(vl1)
            fin = eval(ev)
            tmp.append(fin)
    print(format(round(tmp[0], 2), ".2f"))


solution(lists)
