"""
다익스트라 기반 접근
heapq를 기반으로 구현. 
접근한 지역에 대해선 더 싼 비용으로 접근 가능하다면 업데이트하고 queue에 넣는다
그게 아니라면 queue에 넣지 않고 continue
"""


import sys
import heapq
from collections import defaultdict

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(m):
    s, d, c = map(int, sys.stdin.readline().split(" "))
    graph[s].append((d, c))
s, f_d = map(int, sys.stdin.readline().split(" "))
queue = [(0, s)]
visited_cost = {}
visited_cost[s] = 1e9
heapq.heapify(queue)
while queue:
    c, s = heapq.heappop(queue)
    if visited_cost[s] < c:
        continue
    for d in graph[s]:
        n_s, n_c = d[0], c + d[1]
        if n_s not in visited_cost:
            visited_cost[n_s] = n_c
            heapq.heappush(queue, (n_c, n_s))
            continue
        if visited_cost[n_s] > n_c:
            visited_cost[n_s] = n_c
            heapq.heappush(queue, (n_c, n_s))

print(visited_cost[f_d])
