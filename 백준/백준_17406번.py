import copy
import itertools

n, m, k = list(map(int, input().split(" ")))
mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)
cases = []
for _ in range(k):
    row = list(map(int, input().split(" ")))
    cases.append(row)
comb_cases = list(itertools.permutations(cases, k))


def rotate(mat, case):
    left_top = (case[0] - case[2] - 1, case[1] - case[2] - 1)
    right_down = (case[0] + case[2] - 1, case[1] + case[2] - 1)
    tmp_mat = copy.deepcopy(mat)
    while left_top != right_down:
        tmp_col = left_top[1]
        tmp_row = left_top[0]
        max_col = right_down[1]
        max_row = right_down[0]
        min_col = left_top[1]
        min_row = left_top[0]
        while True:
            if tmp_col == max_col:
                break
            tmp_col += 1
            tmp_mat[tmp_row][tmp_col] = mat[tmp_row][tmp_col - 1]
        while True:
            if tmp_row == max_row:
                break
            tmp_row += 1
            tmp_mat[tmp_row][tmp_col] = mat[tmp_row - 1][tmp_col]
        while True:
            if tmp_col == min_col:
                break
            tmp_col -= 1
            tmp_mat[tmp_row][tmp_col] = mat[tmp_row][tmp_col + 1]
        while True:
            if tmp_row == min_row:
                break
            tmp_row -= 1
            tmp_mat[tmp_row][tmp_col] = mat[tmp_row + 1][tmp_col]
        left_top = (left_top[0] + 1, left_top[1] + 1)
        right_down = (right_down[0] - 1, right_down[1] - 1)
    return tmp_mat


fin_min = 1000000
for comb_case in comb_cases:
    tmp_mat = copy.deepcopy(mat)
    min_val = 1000000
    for case in comb_case:
        tmp_mat = rotate(tmp_mat, case)
    for row in tmp_mat:
        val = sum(row)
        min_val = min(val, min_val)
    fin_min = min(min_val, fin_min)
print(fin_min)
