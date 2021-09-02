import collections
import copy
import math

# 자료 구축
n, l, r = list(map(int, input().split(" ")))
mat = []
visit = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    vis_row = [0] * n
    mat.append(row)
    visit.append(vis_row)

# bfs로 국경을 여는 나라 탐색
def bfs(mat, l, r, visit, i, j):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [(i, j)]  # 이걸 통해 인구수 구함
    queue = collections.deque([(i, j)])
    visit[i][j] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and l <= abs(mat[x][y] - mat[nx][ny]) <= r
                and (nx, ny) not in visited
                and visit[nx][ny] != 1
            ):
                visited.append((nx, ny))
                queue.append((nx, ny))
                visit[nx][ny] = 1
    return visited


open_count = 0 # 최종 값
while True:
    tmp_visit = copy.deepcopy(visit) # 매번 변하기 때문에 copy
    tmp_mat = copy.deepcopy(mat) # 매번 변하기 때문에 copy
    count_g = 0
    for i in range(n):
        for j in range(n):
            if tmp_visit[i][j] != 1: # visit한 곳은 탐색에서 제외
                gate_cont = bfs(mat, l, r, tmp_visit, i, j)
                sum_people = 0 # 이걸로 사람 수 구하기
                if len(gate_cont) == 1: # 이건 국경을 열 수 없다는 의미
                    continue
                for cont in gate_cont: # 사람 수 구하기
                    sum_people += mat[cont[0]][cont[1]]
                mean_people = math.trunc(sum_people / len(gate_cont)) # 평균 사람 수가 들어가게 됨
                for cont in gate_cont:
                    tmp_mat[cont[0]][cont[1]] = mean_people
                if sum_people:
                    count_g += 1 # 이걸로 끝 여부 정한다.

    mat = tmp_mat # 나라 인구수 갱신
    if not count_g: # count_g가 0이면 어떤 나라도 국경을 열어주지 않음 
        break
    open_count += 1 # open 횟수

print(open_count)
