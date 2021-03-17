n = int(input())
days = []
prices = []
dp = []
for _ in range(n):
    day, price = list(map(int, input().split(" ")))
    days.append(day)
    prices.append(price)
    dp.append(price)
dp.append(0)

def solution(days, prices, dp, n):
    for i in range(n-1, -1, -1):
        if days[i] + i > n:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(prices[i] + dp[i + days[i]], dp[i+1])
    return dp[0]

print(solution(days,prices, dp, n))