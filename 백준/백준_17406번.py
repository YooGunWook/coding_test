import copy
import itertools

# 데이터 구성
n, m, k = list(map(int, input().split(" ")))
mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)
cases = []
for _ in range(k):
    row = list(map(int, input().split(" ")))
    cases.append(row)
comb_cases = itertools.permutations(cases, k)  # 순서를 바꿔서도 진행해봐야 함

# 시계방향으로 회전시켜주는 함수
def rotate(mat, case):
    # 각 인덱스가 +1 되어 있기 때문에 빼준다.
    left_top = (case[0] - case[2] - 1, case[1] - case[2] - 1)
    right_down = (case[0] + case[2] - 1, case[1] + case[2] - 1)
    tmp_mat = copy.deepcopy(mat)  # 돌릴 행렬을 copy해준다
    while left_top != right_down:
        tmp_col = left_top[1]  # 좌표
        tmp_row = left_top[0]  # 좌표
        max_col = right_down[1]  # max
        max_row = right_down[0]  # max
        min_col = left_top[1]  # min
        min_row = left_top[0]  # min
        # 시계방향으로 돌려주기
        while True:  # 오른쪽 끝으로 가는 케이스
            if tmp_col == max_col:
                break
            tmp_col += 1
            tmp_mat[tmp_row][tmp_col] = mat[tmp_row][tmp_col - 1]
        while True:  # 오른쪽의 밑 끝으로 가는 케이스
            if tmp_row == max_row:
                break
            tmp_row += 1
            tmp_mat[tmp_row][tmp_col] = mat[tmp_row - 1][tmp_col]
        while True:  # 왼쪽 끝으로 가는 케이스
            if tmp_col == min_col:
                break
            tmp_col -= 1
            tmp_mat[tmp_row][tmp_col] = mat[tmp_row][tmp_col + 1]
        while True:  # 왼쪽 윗 끝으로 가는 케이스
            if tmp_row == min_row:
                break
            tmp_row -= 1
            tmp_mat[tmp_row][tmp_col] = mat[tmp_row + 1][tmp_col]
        # 중앙으로 둘의 간격을 좁혀준다.
        left_top = (left_top[0] + 1, left_top[1] + 1)  # 얘는 하나씩 올리기
        right_down = (right_down[0] - 1, right_down[1] - 1)  # 얘는 하나씩 줄이기
    return tmp_mat


fin_min = 1000000
for comb_case in comb_cases:  # 각 케이스별로 진행한다.
    tmp_mat = mat  # matrix 복사해주기
    for case in comb_case:  # 돌려주기
        tmp_mat = rotate(tmp_mat, case)
    for row in tmp_mat:  # 최소 행렬값 구하기
        val = sum(row)
        if fin_min > val:
            fin_min = val
print(fin_min)
