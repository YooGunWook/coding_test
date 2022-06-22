"""
DP 기반 풀이 
visited[-1][-1]에 도달할 경우의 수 구해야함. 
visited[i][j]가 0이 아니어야 움직일 수 있기 때문에 처음은 1로 진행.
그 다음에 0이 아닌 방향으로 쭉 이동해야한다. 
i + mat[i][j] < n 이면 아래 방향으로 움직이고,
j + mat[i][j] < n 이면 오른쪽으로 움직인다.
"""

n = int(input())
mat = []
visited = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)
    visited.append([0] * n)

visited[0][0] = 1
for i in range(n):
    for j in range(n):
        if visited[i][j] != 0 and mat[i][j] != 0:
            if i + mat[i][j] < n:
                visited[i + mat[i][j]][j] += visited[i][j]
            if j + mat[i][j] < n:
                visited[i][j + mat[i][j]] += visited[i][j]

print(visited[-1][-1])
