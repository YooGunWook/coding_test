"""
DP 문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때,
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

- 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
- N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
- i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
"""

n = int(input())
color_list = []
for _ in range(n):
    colors = list(map(int, input().split(" ")))
    color_list.append(colors)


# dp로 문제 풀이
def solution(n, color_list):
    dp = []  # 집별 가격을 담는 DP list
    for i in range(0, n):
        tmp_dp = [0] * 3
        if i == 0:
            for price_idx in range(0, 3):  # 첫번째 집은 다른 것은 고려하지 않아도 되기 때문에 바로 넣는다.
                tmp_dp[price_idx] = color_list[i][price_idx]
            dp.append(tmp_dp)
        else: # 첫번째 집을 제외하고 최적의 집값을 선택해야한다.
            # i-1과 i+1과는 다른 색으로 진행해야되기 때문에 여러 케이스로 진행한다. 
            for price_idx in range(0, 3): 
                if price_idx == 0: # 해당 집에 빨간색을 칠할 때
                    value = min(
                        color_list[i][price_idx] + dp[i - 1][price_idx + 1],
                        color_list[i][price_idx] + dp[i - 1][price_idx + 2],
                    )
                elif price_idx == 1: # 해당 집에 초록색을 칠할 때
                    value = min(
                        color_list[i][price_idx] + dp[i - 1][price_idx - 1],
                        color_list[i][price_idx] + dp[i - 1][price_idx + 1],
                    )
                else: # 해당 집에 노란색을 칠할 때
                    value = min(
                        color_list[i][price_idx] + dp[i - 1][price_idx - 1],
                        color_list[i][price_idx] + dp[i - 1][price_idx - 2],
                    )
                tmp_dp[price_idx] = value
            dp.append(tmp_dp)
    return min(dp[-1])


print(solution(n, color_list))
