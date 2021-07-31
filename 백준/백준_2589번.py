"""
보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 
보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 
각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다. 
보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 
육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.

예를 들어 위와 같이 지도가 주어졌다면 보물은 아래 표시된 두 곳에 묻혀 있게 되고, 이 둘 사이의 최단 거리로 이동하는 시간은 8시간이 된다.
보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.
"""
from collections import deque

m, n = list(map(int, input().split(" ")))
mat = []
for _ in range(m):
    row = list(input())
    mat.append(row)


def bfs(mat, i, j):
    di = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 방향
    queue = deque([(i, j, 0)])  # 시작
    visited = [[0] * n for _ in range(m)]  # 방문 체크. 이걸로 최단 거리 체크
    visited[i][j] = 1  # 시작은 1로 지정한다.
    max_dist = 0  # 최장 거리가 보물이 있는 위치
    while queue:
        x, y, time = queue.popleft()
        for idx in range(4):
            mx = x + di[idx][0]
            ny = y + di[idx][1]
            if (
                0 <= mx < m
                and 0 <= ny < n
                and mat[mx][ny] == "L"
                and visited[mx][ny] != 1
            ):
                visited[mx][ny] = 1

                queue.append((mx, ny, time + 1))

                if max_dist < time:  # 최장 시간 업데이트를 진행함.
                    max_dist = time

    return time


max_dist = 0
for i in range(m):  # 각각 체크를 해줘야함.
    for j in range(n):
        if mat[i][j] == "L":
            res = bfs(mat, i, j)
            # print(res)
            if max_dist < res:
                max_dist = res  # 가장 긴 부분이 보물 위치이기 때문에 최장거리 체크
print(max_dist)

