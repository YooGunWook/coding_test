import copy
from collections import deque
import time

n, m = list(map(int, input().split(" ")))
mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)


def bfs():
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque([(0, 0)])
    visited = []
    for _ in range(n):
        row = [-1] * m
        visited.append(row)
    visited[0][0] = 0
    while queue:
        print(queue)
        time.sleep(0.5)
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < n and 0 <= nx < m:
                if visited[ny][nx] == -1:
                    if mat[ny][nx] >= 1:
                        mat[ny][nx] += 1
                    else:
                        visited[ny][nx] = 0
                        queue.append((ny, nx))


count = 0
while True:
    bfs()
    cnt = 0
    for i in mat:
        print(i)
    print()
    for i in range(n):
        for j in range(m):
            if mat[i][j] >= 3:
                mat[i][j] = 0
                cnt = 1
            elif mat[i][j] == 2:
                mat[i][j] = 1
    if cnt == 1:
        count += 1
    else:
        break
print(count)