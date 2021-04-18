n, m = list(map(int, input().split(" ")))
mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)


# 최대값을 만들어주는 함수
def flag(mat, i, j, squares):
    fin_sum = []  # 최종 sum 값을 저장해주는 함수
    for square in squares:  # 각 케이스 별 조회
        sum_list = []
        flag = True  # True: index 초과 안함 False: index 초과
        for value in square:  # 각 케이스의 형태로 만들어주기
            new_n = i + value[0]
            if 0 > new_n or new_n > n - 1:  # index 초과 케이스
                flag = False
                break
            new_m = j + value[1]
            if 0 > new_m or new_m > m - 1:  # index 초과 케이스
                flag = False
                break
            sum_list.append(mat[new_n][new_m])  # # index 초과 안하면 sum_list에 넣어준다.
        if flag == False:  # 4개가 다 안들어가기 때문에 0으로 처리
            fin_sum.append(0)
        fin_sum.append(sum(sum_list))  # 4개가 다 들어갔기 때문에 합해서 넣어준다.
    return fin_sum


def square(mat, i, j):  # 정사각형 케이스
    square_max = 0
    sum_square = 0
    squares = [[(0, 0), (0, 1), (1, 0), (1, 1)]]  # 정사각형을 만들어줄 수 있는 좌표
    sum_square = max(flag(mat, i, j, squares))  # flag를 통해 나온 최댓값
    if square_max < sum_square:
        square_max = sum_square
    return square_max


def row(mat, i, j):  # 한줄로 된 케이스
    row_max = 0
    sum_row = 0
    row_row = [(0, 0), (0, 1), (0, 2), (0, 3)]  # 가로 형태
    row_col = [(0, 0), (1, 0), (2, 0), (3, 0)]  # 세로 형태
    row_dir = [row_row, row_col]
    # row first
    sum_row = max(flag(mat, i, j, row_dir))
    if sum_row > row_max:
        row_max = sum_row
    return row_max


def angle(mat, i, j):  # 직각 형태 케이스
    angle_max = 0
    sum_angle = 0
    # 회전, 반전 모두 적용
    angle_1 = [(0, 0), (0, 1), (-1, 1), (-2, 1)]
    angle_2 = [(0, 0), (0, 1), (-1, 0), (-2, 0)]
    angle_3 = [(0, 0), (0, 1), (1, 1), (2, 1)]
    angle_4 = [(0, 0), (0, 1), (1, 0), (2, 0)]
    angle_5 = [(0, 0), (0, 1), (0, 2), (1, 2)]
    angle_6 = [(0, 0), (0, 1), (0, 2), (1, 0)]
    angle_7 = [(0, 0), (0, 1), (0, 2), (-1, 2)]
    angle_8 = [(0, 0), (0, 1), (0, 2), (-1, 0)]
    angles = [angle_1, angle_2, angle_3, angle_4, angle_5, angle_6, angle_7, angle_8]
    sum_angle = max(flag(mat, i, j, angles))
    if sum_angle > angle_max:
        angle_max = sum_angle
    return sum_angle


def zigzag(mat, i, j):  # 지그재그 형태
    zigzag_max = 0
    sum_zigzag = 0
    # 지그재그 형태의 모든 좌표
    zigzag_1 = [(0, 0), (1, 0), (1, 1), (2, 1)]
    zigzag_2 = [(0, 0), (1, 0), (1, -1), (2, -1)]
    zigzag_3 = [(0, 0), (0, 1), (-1, 1), (-1, 2)]
    zigzag_4 = [(0, 0), (0, 1), (1, 1), (1, 2)]
    zigzags = [zigzag_1, zigzag_2, zigzag_3, zigzag_4]
    sum_zigzag = max(flag(mat, i, j, zigzags))
    if sum_zigzag > zigzag_max:
        zigzag_max = sum_zigzag
    return zigzag_max


def T(mat, i, j):  # T자 형태
    T_max = 0
    sum_T = 0
    # T자 형태의 모든 좌표
    T_1 = [(0, 0), (0, 1), (0, 2), (1, 1)]
    T_2 = [(0, 0), (1, 0), (2, 0), (1, 1)]
    T_3 = [(0, 0), (0, 1), (0, 2), (-1, 1)]
    T_4 = [(0, 0), (1, 0), (2, 0), (1, -1)]
    Ts = [T_1, T_2, T_3, T_4]
    sum_T = max(flag(mat, i, j, Ts))
    if sum_T > T_max:
        T_max = sum_T
    return T_max


max_val = 0
for i in range(n):
    for j in range(m):
        # 각 좌표별로 최대값을 구해준다.
        # 어차피 index 넘기면 0이 되기 때문에 그냥 진행한다.
        t = T(mat, i, j)
        zig = zigzag(mat, i, j)
        r = row(mat, i, j)
        squ = square(mat, i, j)
        ang = angle(mat, i, j)
        # 각 케이스별로 최대값으로 바꿔준다.
        max_val = max(max_val, t, zig, r, squ, ang)
print(max_val)
