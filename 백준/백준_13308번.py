# 이동하기 전에 기름을 넣고 출발
# 기름통 크기는 무제한
# 1km 당 1리터
# 각 도시마다 하나의 주유소, 주유소마다 리터당 가격은 다를 수 있음.

"""
  0 1 2 3 4 
0 0 0 0 0 0  
1 0 0 
2 0 
3 0 
4 0 
"""

import heapq

n, m = list(map(int, input().split(" ")))
fuel_list = list(map(int, input().split(" ")))
fuel_cost_city = {i + 1: fuel_list[i] for i in range(n)}
graph_city = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    c1, c2, cost = list(map(int, input().split(" ")))
    graph_city[c1][c2] = cost
    graph_city[c2][c1] = cost
# graph_city[0][1] = fuel_cost_city[1]
# graph_city[1][0] = fuel_cost_city[1]

dp = [[0] * 6 for _ in range(6)]
chk = [[0] * 6 for _ in range(6)]

queue = [(0, fuel_cost_city[1], 1)]
heapq.heapify(queue)

while queue:
    cost, low_cost, idx = heapq.heappop(queue)
    if idx == n:
        print(cost)
        break
    for i in range(1, n + 1):
        n_low_cost = min(low_cost, fuel_cost_city[i])
        n_cost = cost + graph_city[idx][i] * n_low_cost
        if graph_city[idx][i] != 0 and chk[idx][n_low_cost] != 1:
            dp[i][n_low_cost] = n_cost
            chk[i][n_low_cost] = 1
            heapq.heappush(
                queue,
                (n_cost, n_low_cost, i),
            )
