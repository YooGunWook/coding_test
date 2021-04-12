n = int(input())
dp = [j for j in range(n + 1)]
print(dp)
for idx, value in enumerate(dp):
    if idx == 0:
        continue
    if idx == 1 or idx == 2:
        dp[idx] = 1
        continue
    dp[idx] = dp[idx - 1] + dp[idx - 2]

print(dp[n])
