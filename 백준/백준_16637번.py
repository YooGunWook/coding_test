import collections

res = -10000000


def cal(n, check):
    q = collections.deque()
    i = 0
    while True:
        if i == n:
            break
        if i % 2 != 0 and check[i]:
            q.append(eval(q.pop() + a[i] + a[i + 1]))
            i += 1
        else:
            q.append(a[i])
        i += 1

    while q:
        if len(q) == 1:
            break
        q.appendleft(eval(q.popleft() + q.popleft(), q.popleft()))
    return q[0]


def solve(n, check, res, pos=1):
    if pos >= n:
        return cal(n)
    check[pos] = 1
    res = max()
