"""
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 
따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.
크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 
그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)
예를 들어, 그림이 아래와 같은 경우에
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 
하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)
그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.
"""

import collections

n = int(input())
mat = []  # 적록색약이 아닌 케이스
non_mat = []  # 적록색약인 케이스
visited = []
non_visited = []
for _ in range(n):
    row = list(input())
    n_row = []
    for i in row:
        if i == "R" or i == "G":
            n_row.append("RG")
        else:
            n_row.append(i)
    v_row = [0] * n
    nv_row = [0] * n
    mat.append(row)
    non_mat.append(n_row)
    visited.append(v_row)
    non_visited.append(nv_row)

# 개수 카운트 용
nor_dict = {"R": 0, "G": 0, "B": 0}
non_dict = {"RG": 0, "B": 0}


def bfs(mat, r, c, color, visited):
    di = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = collections.deque([(r, c)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + di[i][0]
            ny = y + di[i][1]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and visited[nx][ny] != 1
                and mat[nx][ny] == color
            ):
                visited[nx][ny] = 1
                queue.append((nx, ny))
    return 1


for i in range(n):
    for j in range(n):
        # 적록색약인 케이스와 아닌 케이스를 나눔.
        if visited[i][j] != 1:
            count = bfs(mat, i, j, mat[i][j], visited)
            nor_dict[mat[i][j]] += 1
        if non_visited[i][j] != 1:
            count = bfs(non_mat, i, j, non_mat[i][j], non_visited)
            non_dict[non_mat[i][j]] += 1


print(f"{sum(nor_dict.values())} {sum(non_dict.values())}")
