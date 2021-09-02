n, m, k = list(map(int, input().split(" ")))
mat = []
for _ in range(n):
    row = [0] * m
    mat.append(row)
for _ in range(k):
    x, y = list(map(int, input().split(" ")))
    mat[x - 1][y - 1] = 1

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(i, j, visited):
    stack = [(i, j)]
    count = 0
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and mat[nx][ny] == 1
                and visited[nx][ny] == 0
            ):
                stack.append((nx, ny))
                visited[nx][ny] = 1
                count += 1
    return count


def solution(mat):
    visited = []
    count = 0
    for _ in range(n):
        row = [0] * m
        visited.append(row)
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1 and visited[i][j] == 0:
                count = max(count, dfs(i, j, visited))
    return count


print(solution(mat))
