import collections

# 데이터 만들기
n, m = map(int, input().split(" "))
mat = []  # 실제 병사들 위치 파악용
visited = []  # 방문한 노드 확인용
for _ in range(m):
    row = list(input())
    row_visit = [0 for _ in range(n)]
    mat.append(row)
    visited.append(row_visit)


# bfs로 구현
def bfs(mat, visited, i, j, target):
    # i == n, j == m
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # direction
    queue = collections.deque([(j, i)])  # bfs는 queue로 구현
    visited[j][i] = 1  # 방문 기록
    count = 1  # 1부터 시작
    while queue:
        y, x = queue.popleft()
        for idx in range(4):  # 4면을 bfs로 조회
            nx = x + dx[idx]
            ny = y + dy[idx]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and visited[ny][nx] == 0
                and mat[ny][nx] == target
            ):  # 이 조건 안에 있어야 queue에 저장하고 방문기록 남김
                queue.append((ny, nx))
                visited[ny][nx] = 1
                count += 1
    return count


b_count = 0  # 파란팀
w_count = 0  # 흰팀
# 각 노드 조회하기
for i in range(n):
    for j in range(m):
        if visited[j][i] == 0:  # 방문한 친구가 아니면 이 친구부터 시작
            target = mat[j][i]  # 무슨 색상 팀인지 파악
            count = bfs(mat, visited, i, j, target)
            if target == "B":
                b_count += count ** 2  # count**2만큼의 파워가 생김
            elif target == "W":
                w_count += count ** 2  # count**2만큼의 파워가 생김

print(w_count, b_count)
