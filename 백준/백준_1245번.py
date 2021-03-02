n, m = list(map(int, input().split(" ")))
mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)

dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]


def check_dis(res):
    for prob in res:
        x, y = prob
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if mat[x][y] < mat[nx][ny]:
                    return False
    return True


def dfs(i, j, visited):
    stack = [(i, j)]
    visited[i][j] = 1
    res = [(i, j)]
    while stack:
        x, y = stack.pop()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if mat[nx][ny] == mat[x][y]:
                    stack.append((nx, ny))
                    res.append((nx, ny))
                    visited[nx][ny] = 1
    print(res)
    for i in visited:
        print(i)
    print()
    if check_dis(res) == False:
        return False
    return True


def solution():
    visited = []
    count = 0
    for _ in range(n):
        row = [0] * m
        visited.append(row)
    for i in range(m):
        for j in range(n):
            if visited[j][i] == 0:
                res = dfs(j, i, visited)
                if res == True:
                    count += 1
    return count


print(solution())