"""
플로이드 와샬 기반 풀이
"""

n, m = list(map(int, input().split(" ")))
graph = [[1e9] * n for _ in range(n)]

for _ in range(m):
    i, j = list(map(int, input().split(" ")))
    graph[i - 1][j - 1] = 1
    graph[j - 1][i - 1] = 1

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[j][k])

ans = (1e9, 1e9)
for idx, row in enumerate(graph):
    r_sum = sum(row)
    if r_sum == ans[1]:
        if idx + 1 < ans[0]:
            ans = (idx + 1, r_sum)
    elif r_sum < ans[1]:
        ans = (idx + 1, r_sum)

print(ans[0])
