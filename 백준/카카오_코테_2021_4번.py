import collections
from heapq import heappush, heappop


def solution(n, s, a, b, fares):
    graph = collections.defaultdict(list)
    for i in fares:
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0], i[2]))
    queue = [(s, 0)]
    dist = collections.defaultdict(int)
    a_res = 1000000000000000
    b_res = 1000000000000000
    while queue:
        print(queue)
        node, fare = heappop(queue)
        if node == a:
            a_res = min(fare, a_res)
            print(a_res)
        if node == b:
            b_res = min(fare, b_res)
            print(b_res)
        if node not in dist:
            dist[node] = fare
            for new, fa in graph[node]:
                alt = fare + fa
                heappush(queue, (new, alt))
    print(a_res, b_res)
    print(a_res + b_res)


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
    solution(n, s, a, b, fare)
