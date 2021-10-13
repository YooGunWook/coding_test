n = int(input())
mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)
con = list(input())
p = int(input())
dp = [1e9] * (1 << n)

dp[0] = 0


def bit_counting(x):
    # 몇명이 작업에 투입되었는지? --> 비트에 포함된 1의 개수 세기
    answer = 0
    while x:
        answer += x & 1
        x >>= 1
    return answer


def solution(dp, con, mat):
    if con.count("Y") == 0:
        return -1

    for i in range(1 << n):
        k = bit_counting(i)
        for j in range(n):
            tmp = i & 1 << j
            if not tmp:
                chk = i | 1 << j
                if con[k] == "Y":
                    continue
                dat = min(dp[chk], dp[i] + mat[k][j])
                dp[chk] = dat
    return dp[-1]


print(solution(dp, con, mat))
