"""
BFS 문제
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
"""

from collections import deque
import time

n, m = list(map(int, input().split(" ")))
mat = []
visited = []
wall_visited = []
for _ in range(n):
    row = list(map(int, list(input())))
    mat.append(row)
visited = [
    [[0 for _ in range(m)] for _ in range(n)] for _ in range(2)
]  # 0: 벽 뚫는 케이스 1: 벽 뚫지 않는 케이스


def bfs(mat, fin_visited, n, m):
    if n == 1 and m == 1:  # 둘 다 1일 경우 그대로 1 출력
        return 1
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # 방향
    queue = deque([(0, 0, 1, 1)])  # 처음 시작 부분
    count_arrive = 10000000000  # 최소 거리 측정용
    while queue:  # bfs 기반 탐색
        x, y, chance, count = queue.popleft()
        for i in range(len(direction)):  # 네 방향 모두 조회
            nx = x + direction[i][0]
            my = y + direction[i][1]

            if 0 <= nx < n and 0 <= my < m and fin_visited[chance][nx][my] == 0:
                if mat[nx][my] == 1:  # 벽인 경우
                    if chance == 1:  # 벽을 뚫을 찬스가 있음
                        queue.append((nx, my, 0, count + 1))  # 업데이트 진행
                        fin_visited[0][nx][my] = 1  # 벽 뚫는 케이스로만 진행한다.
                        continue
                else:
                    queue.append(
                        (nx, my, chance, count + 1)
                    )  # 벽을 뚫던 안뚫던 chance를 기반으로 인덱싱
                    fin_visited[chance][nx][my] = 1  # visisted는 업데이트 해준다

            if nx == n - 1 and my == m - 1 and count + 1 < count_arrive:  # 최종에 도달 했을 때
                count_arrive = count + 1
        # for visit in fin_visited:
        #     for row in visit:
        #         print(row)
        #     print()
        # print()
        # time.sleep(0.2)

    if count_arrive == 10000000000:  # 도달하지 못할 경우
        return -1
    return count_arrive


print(bfs(mat, visited, n, m))
