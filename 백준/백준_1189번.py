r, c, k = list(map(int, input().split(" ")))
mat = []
for _ in range(r):
    row = list(input())
    mat.append(row)
visited = []
for _ in range(r):
    row = [0] * c
    visited.append(row)
ans = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y, count, end):
    global ans
    if (x, y) == end and count == k:
        ans += 1
        return

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if 0 <= nx < r and 0 <= ny < c:
            if visited[nx][ny] == 0 and mat[nx][ny] == ".":
                visited[nx][ny] = 1
                dfs(nx, ny, count + 1, end)
                visited[nx][ny] = 0
    return ans


def solution():
    start = (r - 1, 0)
    visited[r - 1][0] = 1
    end = (0, c - 1)
    count = 1
    res = dfs(start[0], start[1], count, end)
    return res


solution()
print(ans)