from collections import deque

"""
BFS 기반 접근
visited mat와 mat를 만들어서 bfs 조회를 한다.
bfs 조회시 (row, col, day)로 해서 며칠이 지났는지 계속 카운트 한다. -> 한번에 변하기 때문에 이렇게 해줘야함.
이미 방문한 곳은 시간 절약을 위해 pass할 수 있게 한다.
"""

c, r = map(int, input().split(" "))
mat = []
visited = []
for _ in range(r):
    row = list(map(int, input().split(" ")))
    mat.append(row)
    visited.append([0] * c)

queue = deque([])
zero_count = 0

for i in range(r):
    for j in range(c):
        if mat[i][j] == 1:
            queue.append((i, j, 0))
        elif mat[i][j] == 0:
            zero_count += 1


def bfs(mat, queue, visited, c, r, zero_count):
    dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while queue:
        tr, tc, day = queue.popleft()
        if visited[tr][tc] == 0:
            visited[tr][tc] = 1
            for d in dr:
                nr = tr + d[0]
                nc = tc + d[1]
                if 0 <= nc < c and 0 <= nr < r and mat[nr][nc] == 0:
                    mat[nr][nc] = 1
                    queue.append((nr, nc, day + 1))
                    zero_count -= 1
    if zero_count != 0:
        return -1
    else:
        return day


print(bfs(mat, queue, visited, c, r, zero_count))
