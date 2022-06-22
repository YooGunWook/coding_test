"""
DP 기반 풀이
[0] * 10을 통해 끝자리가 0~9로 설정해서 진행.
n개만큼의 row를 만들어서 dp 진행
왼쪽값 + 윗쪽 값을 더하면 dp[i][j]의 값이 만들어진다.
"""

n = int(input())
mat = [[0] * 10 for _ in range(n)]
mat[0] = [1] * 10
for _ in range(n):
    mat[_][0] = 1

for i in range(1, n):
    for j in range(1, 10):
        mat[i][j] = mat[i][j - 1] + mat[i - 1][j]

print(sum(mat[n - 1]) % 10007)
