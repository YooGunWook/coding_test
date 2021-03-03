import collections

n, m = list(map(int, input().split(" ")))
mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)


dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]


def bfs(i, j, visited):
    queue = collections.deque([(i, j, 0)])
    while queue:
        print(queue)
        x, y, count = queue.popleft()
        visited[x][y] = 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            while 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if mat[nx][ny] == 1:
                    count += 1
                    return count
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = 1
    return count


def solution(mat):
    res = []
    for i in range(n):
        for j in range(m):
            visited = []
            for _ in range(n):
                row = [0] * m
                visited.append(row)
            if mat[i][j] == 0:
                count = bfs(i, j, visited)
                res.append(count)
    return max(res)


print(solution(mat))
