r, c, k = list(map(int, input().split(" ")))
mat = []
for _ in range(r):
    row = list(input())
    mat.append(row)
visited = []
for _ in range(r):
    row = [0] * c
    visited.append(row)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y, count, end, ans):
    if (x, y) == end and count == k:
        ans += 1
        return

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if 0 <= nx < r and 0 <= ny < c:
            if visited[nx][ny] == 0 and mat[nx][ny] == ".":
                visited[nx][ny] = 1
                for row in visited:
                    print(row)
                print()
                dfs(nx, ny, count + 1, end, ans)
                visited[nx][ny] = 0


def solution():
    start = (r - 1, 0)
    visited[r - 1][0] = 1
    end = (0, c - 1)
    count = 0
    ans = 0
    res = dfs(start[0], start[1], count, end, ans)
    return res
