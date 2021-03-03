import collections
import copy

n, m = list(map(int, input().split(" ")))

mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)

bing_list = []
for i in range(n):
    for j in range(m):
        if mat[i][j] != 0:
            bing_list.append((i, j))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def melting(bing_list, mat):
    check = copy.deepcopy(bing_list)
    tmp_mat = copy.deepcopy(mat)
    for ice in bing_list:
        x, y = ice
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if mat[nx][ny] == 0:
                    tmp_mat[x][y] -= 1
            if tmp_mat[x][y] <= 0:
                tmp_mat[x][y] = 0
                check.remove((x, y))
                break
    return check, tmp_mat


def bfs(check, mat):
    visited = []
    for _ in range(n):
        row = [0] * m
        visited.append(row)
    count = 0
    for bing in check:
        if visited[bing[0]][bing[1]] == 1:
            continue
        queue = collections.deque([bing])
        while queue:
            x, y = queue.popleft()
            visited[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and visited[nx][ny] == 0
                    and mat[nx][ny] != 0
                ):
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
        count += 1
    return count


def solution(bing_list, mat):
    count = 0
    res = 0
    while True:
        res = bfs(bing_list, mat)
        if res >= 2:
            break
        if not bing_list:
            break
        bing_list, mat = melting(bing_list, mat)
        count += 1
    if not bing_list:
        return 0
    return count


print(solution(bing_list, mat))