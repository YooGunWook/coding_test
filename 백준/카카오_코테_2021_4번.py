import collections
from heapq import heappush, heappop


def dijkstra(graph, src, n):
    queue = [(src, 0)]
    dist = collections.defaultdict(int)
    for i in range(1, n + 1):
        dist[i] = 100000000000000
    dist[src] = 0
    while queue:
        node, fare = heappop(queue)
        if dist[node] < fare:
            continue
        for y, cost in graph[node]:
            cost += fare
            if cost < dist[y]:
                dist[y] = cost
                heappush(queue, (y, cost))
    return dist


def solution(n, s, a, b, fares):
    graph = collections.defaultdict(list)
    ans = 10000000000000000
    for i in fares:
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0], i[2]))
    print(graph)
    for k in range(1, n + 1):
        dist_k = dijkstra(graph, k, n)
        print(dist_k)
        if s not in dist_k or a not in dist_k or b not in dist_k:
            continue
        ans = min(ans, dist_k[a] + dist_k[s] + dist_k[b])
        print(ans)
    return ans


if __name__ == "__main__":
    fare = [
        [4, 1, 10],
        [3, 5, 24],
        [5, 6, 2],
        [3, 1, 41],
        [5, 1, 24],
        [4, 6, 50],
        [2, 4, 66],
        [2, 3, 22],
        [1, 6, 25],
    ]
    n = 6
    s = 4
    a = 6
    b = 2
    print(solution(n, s, a, b, fare))
