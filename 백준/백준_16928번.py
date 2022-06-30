"""
bfs 기반 풀이
"""

from collections import deque, defaultdict

n, m = list(map(int, input().split(" ")))
mat = [0] * 101
case = defaultdict(int)
for _ in range(n):
    x, y = list(map(int, input().split(" ")))
    case[x] = y
for _ in range(m):
    u, v = list(map(int, input().split(" ")))
    case[u] = v

queue = deque([(1, 0)])
move = (1, 2, 3, 4, 5, 6)
min_count = 1e9

while queue:
    now, count = queue.popleft()
    if now == 100:
        if min_count > count:
            min_count = count
            continue
    for m in move:
        mn = now + m
        if mn > 100:
            continue
        if mn in case:
            mn = case[mn]
        if mat[mn] != 0:
            if mat[mn] > count + 1:
                mat[mn] = count + 1
                queue.append((mn, count + 1))
        else:
            mat[mn] = count + 1
            queue.append((mn, count + 1))

print(mat[-1])
