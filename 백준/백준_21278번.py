"""
플로이드 와샬 + 브루트 포스 기반 풀이
"""

n, m = list(map(int, input().split(" ")))

mat = [[1e9] * n for _ in range(n)]

for i in range(n):
    mat[i][i] = 0

for _ in range(m):
    a, b = list(map(int, input().split(" ")))
    mat[a - 1][b - 1] = 1
    mat[b - 1][a - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])

# for row in mat:
#     print(row)

ans = [0, 0, 1e9]
for i in range(n - 1):
    for j in range(i, n):
        sum_val = 0
        for k in range(n):
            sum_val += min(mat[k][i], mat[k][j]) * 2
        if ans[2] > sum_val:
            ans = [i + 1, j + 1, sum_val]
            
for idx, a in enumerate(ans):
    if idx == len(ans) - 1:
        print(a)
    else:
        print(a, end=" ")
