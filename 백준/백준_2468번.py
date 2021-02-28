import collections

n = int(input())
mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)


def bfs(x, y, height, visited):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = collections.deque([(x, y, 1)])
    while queue:
        x, y, count = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if mat[nx][ny] > height and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, count))
    return count


result = []
for rain in range(0, 101):
    count = 0
    visited = []
    for _ in range(n):
        row = [0] * n
        visited.append(row)
    for y in range(n):
        for x in range(n):
            if visited[x][y] == 1 or mat[x][y] <= rain:
                continue
            res = bfs(x, y, rain, visited)
            visited[x][y] = 1
            if res == 1:
                count += 1
    result.append(count)
print(max(result))


count = 0
visited = []
for _ in range(n):
    row = [0] * n
    visited.append(row)
for y in range(n):
    for x in range(n):
        if visited[x][y] == 1 or mat[x][y] <= 1:
            continue
        res = bfs(x, y, 1, visited)
        visited[x][y] = 1
        if res == 1:
            count += 1