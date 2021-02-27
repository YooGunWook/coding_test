import collections

n = int(input())
apart = []
for _ in range(n):
    row = list(map(int, input()))
    apart.append(row)

res = []
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    aprt_count = 1
    queue = collections.deque([(x, y)])
    apart[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if apart[nx][ny] == 1:
                    queue.append((nx, ny))
                    apart[nx][ny] = 0
                    aprt_count += 1

    return aprt_count


for y in range(n):
    for x in range(n):
        if apart[x][y] == 1:
            res.append(bfs(x, y))
print(len(res))
for i in res:
    print(i)