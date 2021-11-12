"""
DP 문제
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 
그 경우의 수를 구하시오.
각각의 동전은 몇 개라도 사용할 수 있다.
사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.
"""

n, k = list(map(int, input().split(" ")))
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

# DP로 문제 풀이
def solution(n, k, coins):
    coins = sorted(coins)  # 우선 coin을 sorting한다.
    for i in range(n):  # 각 동전 value에 대해서 조회
        tmp_dp = [0] * k  # tmp_dp를 만든다.
        for value in range(1, k + 1):  # 최대만큼 체크
            if i == 0:  # 동전이 제일 처음 케이스일 경우애는 나머지가 없을 때 모두 1로 지정
                if value % coins[i] == 0:
                    tmp_dp[value - 1] = 1
                    continue
            else:  # 처음 케이스가 아닐 때
                if value < coins[i]:  # value보다 작을 경우 그대로 넣는다
                    tmp_dp[value - 1] = dp[value - 1]
                    continue
                elif value % coins[i] == 0:  # 나눠서 떨어질 경우
                    if value // coins[i] == 1:  # 1로 나눠질 때
                        tmp_dp[value - 1] = dp[value - 1] + (value // coins[i])
                    else:  # 그게 아닐 경우
                        tmp_dp[value - 1] = tmp_dp[value - coins[i] - 1] + dp[value - 1]
                else:  # 그 외 케이스
                    tmp_dp[value - 1] = tmp_dp[value - coins[i] - 1] + dp[value - 1]

        dp = tmp_dp  # dp를 저장해준다.

    return dp[-1]


print(solution(n, k, coins))

