import collections

# 데이터 만들기
mat = []
for _ in range(12):
    row = list(input())
    mat.append(row)

# bfs 탐색 코드
def bfs(mat, i, j, puyo_type, visited, tmp_visited):
    queue = collections.deque([(i, j)])
    visited.append((i, j))  # 모든 visited 정보
    tmp_visited.append((i, j))  # 특정 type에 대한 visited 정보
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    break_count = 1  # 하나로 시작한다.

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + direction[k][0]
            ny = y + direction[k][1]
            if (
                0 <= nx < 12
                and 0 <= ny < 6
                and (nx, ny) not in visited
                and mat[nx][ny] == puyo_type
            ):
                break_count += 1
                visited.append((nx, ny))
                tmp_visited.append((nx, ny))
                queue.append((nx, ny))

    return break_count


fin_break_count = 0  # 최종 break count
while True:
    visited = []
    break_point = []
    for i in range(12):
        for j in range(6):
            if mat[i][j] != "." and (i, j) not in visited:
                tmp_visited = []
                puyo_type = mat[i][j]
                break_count = bfs(mat, i, j, puyo_type, visited, tmp_visited)
                if break_count >= 4:  # 4개 이상일 때 break 한다.
                    for k in range(len(tmp_visited)):
                        ni = tmp_visited[k][0]
                        nj = tmp_visited[k][1]
                        mat[ni][nj] = "."
                    break_point += tmp_visited

    # break가 있을 때 한번의 연쇄 폭발이라 한다.
    if break_point:
        fin_break_count += 1

    # break가 없을 때
    if not break_point:
        break

    # break된 후의 mat 데이터 변경
    for point in break_point:
        x = point[0]
        y = point[1]
        nx = x - 1
        while nx >= 0 and mat[nx][y] != ".":
            mat[nx + 1][y] = mat[nx][y]
            mat[nx][y] = "."
            nx -= 1

print(fin_break_count)
