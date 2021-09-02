import collections

n = int(input())
v, e = list(map(int, input().split(" ")))
m = int(input())
graph = collections.defaultdict(list)
for _ in range(m):
    a, b = list(map(int, input().split(" ")))
    graph[a].append(b)
    graph[b].append(a)


def bfs(s, e):
    discovered = []
    count = 0
    queue = collections.deque([(s, count)])
    while queue:
        v, count = queue.popleft()
        if v == e:
            return count
        if v not in discovered:
            count += 1
            discovered.append(v)
            for w in graph[v]:
                if w not in discovered:
                    queue.append((w, count))
    return -1


print(bfs(v, e))
