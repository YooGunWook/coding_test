n = int(input())
mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)
dp = [1e9] * (1 << n)
dp[0] = 0


def bit_counting(x):
    # 몇명이 작업에 투입되었는지? --> 비트에 포함된 1의 개수 세기
    answer = 0
    while x:
        answer += x & 1
        x >>= 1
    return answer


def solution(dp, n):
    for i in range(1 << n):
        k = bit_counting(i) # 사람 수를 체크한다.
        for j in range(n): # 작업별 정보를 체크하기 위해 사용
            tmp = i & (1 << j) # 이게 0이면 새로 갱신하거나 채워짐. 
            if not tmp:
                chk = i | 1 << j # 어떤 걸 사용할 지 정한다. (여태까지 했던 것들 중에서)
                dp[chk] = min(dp[chk], dp[i] + mat[k][j]) # i번째, 즉 현재까지 했던 것에서 업데이트
    return dp[-1]


print(solution(dp, n))
