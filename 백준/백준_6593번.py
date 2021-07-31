"""
당신은 상범 빌딩에 갇히고 말았다. 
여기서 탈출하는 가장 빠른 길은 무엇일까? 
상범 빌딩은 각 변의 길이가 1인 정육면체(단위 정육면체)로 이루어져있다. 
각 정육면체는 금으로 이루어져 있어 지나갈 수 없거나, 비어있어서 지나갈 수 있게 되어있다. 
당신은 각 칸에서 인접한 6개의 칸(동,서,남,북,상,하)으로 1분의 시간을 들여 이동할 수 있다. 
즉, 대각선으로 이동하는 것은 불가능하다. 
리고 상범 빌딩의 바깥면도 모두 금으로 막혀있어 출구를 통해서만 탈출할 수 있다.
당신은 상범 빌딩을 탈출할 수 있을까? 만약 그렇다면 얼마나 걸릴까?
"""
import collections


def bfs(mat, visited, start_index, l, r, c):
    # 동서남북 뿐만 아니라 상하도 있기 때문에 6개로 진행
    di = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
    queue = collections.deque([start_index])
    visited[start_index[0]][start_index[1]][start_index[2]] = 1 # 처음 시작 지점은 이미 방문
    while queue:
        f, x, y, t = queue.popleft()
        if mat[f][x][y] == "E": # 끝나는 지점에 도착하면 시간을 return한다.
            return t
        for i in range(6):
            nf = f + di[i][0]
            nx = x + di[i][1]
            ny = y + di[i][2]
            if (
                0 <= nf < l
                and 0 <= nx < r
                and 0 <= ny < c
                and visited[nf][nx][ny] == 0
                and mat[nf][nx][ny] != "#" # 금으로 덮인 지역
            ):
                visited[nf][nx][ny] = 1
                queue.append((nf, nx, ny, t + 1))

    return -1 # 탈출이 불가능한 케이스


while True:
    data = input() 
    if not data: # 아무것도 입력되지 않는 케이스가 있음. 
        continue

    l, r, c = list(map(int, data.split(" ")))
    if l == 0 and r == 0 and c == 0: # 끝나는 지점
        break

    mat = []
    visited = []

    for _ in range(l):
        tmp_mat = []
        tmp_vi = []
        while len(tmp_mat) != r:
            row = input() # 아무것도 입력 안되는 케이스 있음
            if not row:
                continue
            row = list(row)
            v_row = [0] * c
            tmp_mat.append(row)
            tmp_vi.append(v_row)
        mat.append(tmp_mat)
        visited.append(tmp_vi)

    for f in range(l):
        for i in range(r):
            for j in range(c):
                if mat[f][i][j] == "S": 
                    start_index = (f, i, j, 0) # 시작지점을 받는다.
                    break
    res = bfs(mat, visited, start_index, l, r, c)
    if res != -1:
        print(f"Escaped in {res} minute(s).")
    else:
        print("Trapped!")

