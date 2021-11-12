import heapq

v, e = list(map(int, input().split(" ")))
k = int(input())
graph = {i + 1: [] for i in range(v)}
dist = {i + 1: 1e9 for i in range(v)}
for _ in range(e):
    u, v, w = list(map(int, input().split(" ")))
    graph[u].append((w, v))

# 다익스트라 기반 풀이
def solution(graph, k, dist):
    heap = [(0, k)]  # 시작 부분
    while heap:
        w, v = heapq.heappop(heap)

        if dist[v] < w:  # 만약 더 크면 굳이 볼 필요 없음
            continue

        for edge in graph[v]:  # 새로운 거리 측정
            n_w = edge[0] + w
            n_v = edge[1]
            if n_w < dist[n_v]:  # 원래가 더 클 경우
                dist[n_v] = n_w
                heapq.heappush(heap, (n_w, n_v))
    return dist


dist = solution(graph, k, dist)
for node in dist: # 결과 출력
    if node == k:
        print(0)
    elif dist[node] == 1e9:
        print("INF")
    else:
        print(dist[node])
