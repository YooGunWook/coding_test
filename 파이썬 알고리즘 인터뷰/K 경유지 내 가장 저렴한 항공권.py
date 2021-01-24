import collections
import heapq


def solution(n, edges, src, dst, K):
    graph = collections.defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))

    price = 0
    route = 0
    Q = [(price, route, src)]
    dist = collections.defaultdict(int)

    while Q:
        price, route, start = heapq.heappop(Q)
        if start == dst:
            return price
        if route > K:
            continue
        dist[start] = price
        alt_route = route + 1
        for v, w in graph[start]:
            alt_price = price + w
            heapq.heappush(Q, (alt_price, alt_route, v))
    return -1


if __name__ == "__main__":
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    K = 0
    print(solution(3, edges, src, dst, K))