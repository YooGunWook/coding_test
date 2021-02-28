import collections
import sys

m, n, h = list(map(int, input().split(" ")))

box = []
for _ in range(h):
    floor = []
    for _ in range(n):
        row = list(map(int, input().split(" ")))
        floor.append(row)
    box.append(floor)

visited = []
for _ in range(h):
    floor = []
    for _ in range(n):
        row = [0] * m
        floor.append(row)
    visited.append(floor)


queue = collections.deque([])

for z in range(h):
    for x in range(n):
        for y in range(m):
            if box[z][x][y] == 1 and visited[z][x][y] == 0:
                queue.append((x, y, z))
                visited[z][x][y] = 1


def bfs(queue):
    dx, dy, dh = ([-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1])
    while queue:
        print(visited)
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dh[i]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if box[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                    queue.append((nx, ny, nz))
                    box[nz][nx][ny] = 1
                    visited[nz][nx][ny] = visited[z][x][y] + 1


bfs(queue)
for i in box:
    for j in i:
        if 0 in j:
            print(-1)
            sys.exit()

ans = 0
for i in visited:
    for j in i:
        list_max = max(j)
        ans = max(ans, list_max)
print(ans - 1)