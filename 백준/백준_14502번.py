from itertools import combinations
import collections
import copy

n, m = list(map(int, input().split(" ")))
mat = []
visited = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    visit = [0] * m
    mat.append(row)
    visited.append(visit)

candidates = []  # 벽 세울 리스트 후보들
virus = []  # virus 위치
for i in range(n):
    for j in range(m):
        if mat[i][j] == 0:
            candidates.append((i, j))
        if mat[i][j] == 2:
            virus.append((i, j))

# 조합을 통해 벽 세우는 경우의 수를 만들어준다.
candidate_list = list(combinations(candidates, 3))


# bfs를 통해 바이러스를 퍼트린다.
def bfs(mat, virus, visited):
    dn, dm = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = copy.deepcopy(virus)
    queue = collections.deque(queue)
    while queue:
        i, j = queue.popleft()
        for idx in range(4):
            nn = i + dn[idx]
            nm = j + dm[idx]
            if (
                0 <= nn < n
                and 0 <= nm < m
                and visited[nn][nm] == 0
                and mat[nn][nm] == 0
            ):
                queue.append((nn, nm))
                visited[nn][nm] = 1
                mat[nn][nm] = 2
    return mat


# 바이러스가 퍼진 후에 안전한 장소를 찾는다.
def count_one(mat, i, j, visited):
    dn, dm = [-1, 1, 0, 0], [0, 0, -1, 1]
    count = 1
    queue = collections.deque([(i, j)])
    visited[i][j] = 1
    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            nn = x + dn[idx]
            nm = y + dm[idx]
            if (
                0 <= nn < n
                and 0 <= nm < m
                and visited[nn][nm] == 0
                and mat[nn][nm] == 0
            ):
                queue.append((nn, nm))
                visited[nn][nm] = 1
                count += 1
    return count


max_safe = 0  # 최대 안전지역 개수
for candidate in candidate_list:
    tmp_mat = copy.deepcopy(mat)
    virus_visited = copy.deepcopy(visited)
    # 각 후보별로 벽을 세워서 테스트를 진행한다.
    for idx in candidate:
        tmp_mat[idx[0]][idx[1]] = 1
    tmp_mat = bfs(tmp_mat, virus, virus_visited)
    zero_visited = copy.deepcopy(visited)
    tmp_count = 0  # 벽을 세웠을 때 최대 개수를 계산한다.
    for i in range(n):
        for j in range(m):
            if tmp_mat[i][j] == 0 and zero_visited[i][j] == 0:
                tmp_count += count_one(tmp_mat, i, j, zero_visited)
    max_safe = max(max_safe, tmp_count)
print(max_safe)
