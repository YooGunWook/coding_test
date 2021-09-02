# n = 1,2,3에 대한 값 입력
# 모든 값들은 n-3, n-2, n-1의 출력값을 모두 더한 값임
dp = [0, 1, 2, 4]
for i in range(4, 14):
    dp.append(sum(dp[-3:]))
for _ in range(int(input())):
    print(dp[int(input())])