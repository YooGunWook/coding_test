import collections
import copy
import math

# 데이터 구축
r, c, t = list(map(int, input().split(" ")))
mat = []
for _ in range(r):
    row = list(map(int, input().split(" ")))
    mat.append(row)

# 공기 청정기 위치와 먼지 위치 확인
start_air = []
dust = []
for i in range(r):
    for j in range(c):
        if mat[i][j] > 0:
            dust.append((i, j))
        elif mat[i][j] == -1:
            start_air.append((i, j))
start_air = sorted(start_air, key=lambda x: x[0])  # 가장 위부분부터 시작


def dust_spread(mat, dust):  # 먼지 퍼짐 추가
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = collections.deque(dust)
    tmp_mat = copy.deepcopy(mat)
    while queue:  # 4면으로 진행됨
        x, y = queue.popleft()
        count = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < r and 0 <= ny < c and mat[nx][ny] != -1:
                tmp_mat[nx][ny] += math.trunc(mat[x][y] / 5)
                count += 1
        tmp_mat[x][y] -= math.trunc(mat[x][y] / 5) * count
    return tmp_mat


def new_dust(mat, dust):  # 새로운 먼지 위치 확인
    for i in range(r):
        for j in range(c):
            if mat[i][j] > 0:
                dust.append((i, j))
    return dust


def qurifier_on(mat, start_air):  # 공기 청정기 틀었을 때 먼지 위치 업데이트
    direction = {"right": (0, 1), "left": (0, -1), "up": (-1, 0), "down": (1, 0)}
    tmp_mat = copy.deepcopy(mat)
    for idx, purifier in enumerate(start_air):  # 공기 청정기 별로 확인
        x, y = purifier
        if idx == 0:  # 위 공기 청정기

            direct = direction["right"]
            ny = y + direct[1]
            while ny < c:
                if tmp_mat[x][ny - 1] == -1:
                    tmp_mat[x][ny] = 0
                else:
                    tmp_mat[x][ny] = mat[x][ny - 1]
                ny += direct[1]
                if ny == c:
                    ny -= 1
                    break

            direct = direction["up"]
            nx = x + direct[0]
            while nx >= 0:
                tmp_mat[nx][ny] = mat[nx + 1][ny]
                nx += direct[0]
                if nx == -1:
                    nx += 1
                    break

            direct = direction["left"]
            ny = ny + direct[1]
            while ny >= 0:
                tmp_mat[nx][ny] = mat[nx][ny + 1]
                ny += direct[1]
                if ny == -1:
                    ny += 1
                    break

            direct = direction["down"]
            nx = nx + direct[0]
            while mat[nx][ny] != -1:
                tmp_mat[nx][ny] = mat[nx - 1][ny]
                nx += direct[0]

        elif idx == 1:  # 아래 공기 청정기
            direct = direction["right"]
            ny = y + direct[1]
            while ny < c:
                if tmp_mat[x][ny - 1] == -1:
                    tmp_mat[x][ny] = 0
                else:
                    tmp_mat[x][ny] = mat[x][ny - 1]
                ny += direct[1]
                if ny == c:
                    ny -= 1
                    break

            direct = direction["down"]
            nx = x + direct[0]
            while nx < r:
                tmp_mat[nx][ny] = mat[nx - 1][ny]
                nx += direct[0]
                if nx == r:
                    nx -= 1
                    break

            direct = direction["left"]
            ny = ny + direct[1]
            while ny >= 0:
                tmp_mat[nx][ny] = mat[nx][ny + 1]
                ny += direct[1]
                if ny == -1:
                    ny += 1
                    break

            direct = direction["up"]
            nx = nx + direct[0]
            while mat[nx][ny] != -1:
                tmp_mat[nx][ny] = mat[nx + 1][ny]
                nx += direct[0]

    return tmp_mat


def get_dust_sum(mat):  # 마지막 출력값 계산용. 총 먼지 개수 확인해야함.
    count = 0
    for i in range(r):
        count += sum(mat[i])
    return count + 2


# t초만큼 진행
for _ in range(t):
    new_mat = dust_spread(mat, dust)  # 먼지 퍼지고 난 후
    mat = new_mat
    mat = qurifier_on(mat, start_air)  # 공기 청정기 키고 난 후
    dust = []
    dust = new_dust(mat, dust)  # 새로운 먼지 위치
print(get_dust_sum(mat))
