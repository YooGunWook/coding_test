"""
플로이드 와샬 풀이 
"""

n = int(input())
mat = [[1e9] * n for _ in range(n)]
for _ in range(n - 1):
    k = int(input())
    temp = list(map(int, input().split()))

    for __ in range(k):

        mat[_][temp[__] - 1] = 1

# for i in range(n - 1):
#     mat[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])


def func(n, graph):
    for a in range(n):
        for b in range(n):
            if 0 < graph[0][b] < 1e9:
                if (0 < graph[a][b] < 1e9) and (0 < graph[b][a] < 1e9):
                    return 1
    return 0


print("CYCLE" if func(n, mat) else "NO CYCLE")
