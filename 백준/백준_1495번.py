"""
DP 기반 풀이
노래 개수만큼 row를 만들고, 최대 음량까지 col을 만들어준다. 
그 다음에 직전 음량에서 조절할 수 있는 음량으로 더하기 빼기 해서 가능한 값에 1을 넣어준다.
그다음에 최댓값을 찾아서 return 한다.
"""


n, s, m = list(map(int, input().split(" ")))
v = list(map(int, input().split(" ")))


def solution(n, s, m, v):
    mat = []
    for _ in range(n):
        row = [0] * (m + 1)
        mat.append(row)
    if s + v[0] <= m:
        mat[0][s + v[0]] = 1
    if s - v[0] >= 0:
        mat[0][s - v[0]] = 1

    for i in range(1, n):
        for j in range(0, m + 1):
            if mat[i - 1][j]:
                if j + v[i] <= m:
                    mat[i][j + v[i]] = 1
                if j - v[i] >= 0:
                    mat[i][j - v[i]] = 1
    if sum(mat[-1]) == 0:
        return -1
    ans = 0
    for i in range(m + 1):
        if mat[-1][i] == 1:
            ans = i
    return ans


print(solution(n, s, m, v))
