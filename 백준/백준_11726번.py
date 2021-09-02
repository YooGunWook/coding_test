n = int(input())
# dp 만들기 -> 최대 1000까지 제한 있음
dp = [0, 1, 1] + [0] * 1000


def solution(n, dp):
    # 피보나치 방식으로 구현
    # 재귀 방식으로 구현
    if n < 3:
        return n
    if dp[n] == 0:
        # 이걸 통해서 이전에 구해지지 않은 피보나치 값도 구할 수 있음
        dp[n] = solution(n - 1, dp) + solution(n - 2, dp)
    # dp값 구하기
    return dp[n]


print(solution(n, dp) % 10007)
