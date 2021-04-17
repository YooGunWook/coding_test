def solution(n):
    dp = [0, 0, 1, 1]  # 메모이제이션 방식 활용
    # 0: 단순 인덱스 채우기 1: N이 1일 때 출력값, 2: N이 2일 때 출력값, 3: N이 3일 때 출력값
    for i in range(4, n + 1):
        dp.append(dp[i - 1] + 1)  # 1 빼줄 때
        if i % 2 == 0:  # 2로 나눌 때
            dp[i] = min(dp[i // 2] + 1, dp[i])
        if i % 3 == 0:  # 3으로 나눌 때
            dp[i] = min(dp[i // 3] + 1, dp[i])
    print(dp)
    return dp[n]


while True:
    n = int(input())
    print(solution(n))