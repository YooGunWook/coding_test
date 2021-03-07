import collections
import heapq

a, b = list(map(int, input().split(" ")))
n, m = list(map(int, input().split(" ")))
graph = collections.defaultdict(list)

for _ in range(m):
    i, j = list(map(int, input().split(" ")))
    graph[i].append(j)
    graph[j].append(i)


def bfs(a):
    dist = collections.defaultdict(list)
    queue = [(0, a)]
    while queue:
        time, node = heapq.heappop(queue)
        if node not in dist:
            dist[node] = time
            for v in graph[node]:
                alt = time + 1
                heapq.heappush(queue, (alt, v))
    return dist


def solution(a):
    dist = bfs(a)
    if dist[b] == 0:
        print(-1)
    else:
        print(dist[b])
