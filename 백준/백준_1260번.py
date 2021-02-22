import collections

n, m, v = map(int, input().split(" "))
graph = collections.defaultdict(list)
for _ in range(m):
    g, e = map(int, input().split(" "))
    graph[g].append(e)
    graph[e].append(g)
    graph[g].sort()
    graph[e].sort()


def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered


def iterative_bfs(start_v):
    discovered = [start_v]
    queue = collections.deque([start_v])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered


print(" ".join(map(str, recursive_dfs(v, []))))
print(" ".join(map(str, iterative_bfs(v))))
