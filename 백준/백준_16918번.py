import sys
import collections

r, n, c = list(map(int, input().split(" ")))
mat = []
for _ in range(r):
    row = list(input())
    mat.append(row)


def bfs(mat, queue):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < n:
                mat[x][y] = "."
                mat[nx][ny] = "."
    return mat


if c == 1:
    for row in mat:
        print("".join(row))
    sys.exit()

for time in range(2, c + 1):
    if time % 2 == 0:
        queue = collections.deque([])
        for y in range(n):
            for x in range(r):
                if mat[x][y] == "O":
                    queue.append((x, y))

        mat = []
        for _ in range(r):
            row = ["O"] * n
            mat.append(row)

    elif time % 2 == 1:
        print(queue)
        mat = bfs(mat, queue)
        queue = collections.deque([])

for row in mat:
    print("".join(row))
