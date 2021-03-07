import heapq
import collections


n, m, k, x = list(map(int, input().split(" ")))
graph = collections.defaultdict(list)
for _ in range(m):
    a, b = list(map(int, input().split(" ")))
    graph[a].append(b)


def bfs(x):
    queue = [(0, x)]
    dist = collections.defaultdict(int)
    while queue:
        print(queue)
        time, node = heapq.heappop(queue)
        if node not in dist:
            dist[node] += time
            for v in graph[node]:
                alt = time + 1
                heapq.heappush(queue, (alt, v))
    return dist


def solution(x, k):
    dist = bfs(x)
    print(dist)
    res = []
    for node in dist:
        if dist[node] == k:
            res.append(node)
    if not res:
        print(-1)
    else:
        for i in res:
            print(i)


solution(x, k)
