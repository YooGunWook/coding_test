m, n, k = list(map(int, input().split(" ")))

mat = []
for _ in range(m):
    row = [0] * n
    mat.append(row)
for _ in range(k):
    nx, ny, dx, dy = list(map(int, input().split(" ")))
    for i in range(ny, dy):
        for j in range(nx, dx):
            mat[i][j] = 1
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(i, j, visited):
    stack = [(i, j)]
    count = 1
    visited[i][j] = 1
    while stack:
        for row in visited:
            print(row)
        print()
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < m
                and 0 <= ny < n
                and mat[nx][ny] == 0
                and visited[nx][ny] == 0
            ):
                stack.append((nx, ny))
                visited[nx][ny] = 1
                count += 1
    return count


def solution(mat):
    visited = []
    count = 0
    res = []
    for _ in range(m):
        row = [0] * n
        visited.append(row)
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0 and visited[i][j] == 0:
                each_count = dfs(i, j, visited)
                if each_count == 0:
                    res.append(1)
                    continue
                res.append(each_count)
                count += 1
    res.sort()
    return count, res


count, res = solution(mat)
print(count)
print(" ".join(list(map(str, (res)))))
