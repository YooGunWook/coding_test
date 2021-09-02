import collections
import copy

# 자료 구축
n, m, x, y, k = list(map(int, input().split(" ")))
mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)
order = list(map(int, input().split(" ")))
cube = [0] * 6

# cube 위치를 바꿔주는 함수
def cube_change(cube, order):
    tmp_cube = copy.deepcopy(cube)
    if order == 1:  # 동쪽으로 이동할 때
        tmp_cube[0] = cube[3]
        tmp_cube[2] = cube[0]
        tmp_cube[3] = cube[-1]
        tmp_cube[-1] = cube[2]
    elif order == 2:  # 서쪽으로 이동할 때
        tmp_cube[0] = cube[2]
        tmp_cube[2] = cube[-1]
        tmp_cube[3] = cube[0]
        tmp_cube[-1] = cube[3]
    elif order == 3:  # 북쪽으로 이동할 때
        tmp_cube[0] = cube[4]
        tmp_cube[1] = cube[0]
        tmp_cube[4] = cube[-1]
        tmp_cube[-1] = cube[1]
    elif order == 4:  # 남쪽으로 이동할 때
        tmp_cube[0] = cube[1]
        tmp_cube[1] = cube[-1]
        tmp_cube[4] = cube[0]
        tmp_cube[-1] = cube[4]
    return tmp_cube


# 지도와 주사위 밑칸을 바꾸는 함수
def mat_cube_change(mat, cube, nx, ny):
    # print(cube)
    if mat[nx][ny] == 0:  # 해당 좌표가 0일 때
        mat[nx][ny] = cube[-1]  # 좌표에 주사위 밑칸을 복사
    else:  # 해당 좌표가 0이 아닐 때
        cube[-1] = mat[nx][ny]  # 주사위 밑칸을 좌표의 숫자로 복사
        mat[nx][ny] = 0  # 좌표는 0으로 변환
    # print(cube)
    return mat, cube


def move(order, mat, x, y, cube):  # solution 함수
    queue = collections.deque(order)
    nx = x
    ny = y
    while queue:  # order가 없어질 때까지 진행
        direct = queue.popleft()
        # print(direct)
        # 여기서 and가 추가된 이유는 지도 밖으로 나가는 것을 방지하기 위함
        if direct == 1 and 0 <= ny + 1 < m:
            ny += 1
            cube = cube_change(cube, direct)
            mat, cube = mat_cube_change(mat, cube, nx, ny)
            print(cube[0])

        if direct == 2 and 0 <= ny - 1 < m:
            ny -= 1
            cube = cube_change(cube, direct)
            mat, cube = mat_cube_change(mat, cube, nx, ny)
            print(cube[0])

        if direct == 3 and 0 <= nx - 1 < n:
            nx -= 1
            cube = cube_change(cube, direct)
            mat, cube = mat_cube_change(mat, cube, nx, ny)
            print(cube[0])

        if direct == 4 and 0 <= nx + 1 < n:
            nx += 1
            cube = cube_change(cube, direct)
            mat, cube = mat_cube_change(mat, cube, nx, ny)
            print(cube[0])


print(move(order, mat, x, y, cube))