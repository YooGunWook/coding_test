from collections import deque

n = int(input())
m = int(input())
graph = {i + 1: [] for i in range(n)}

for _ in range(m):
    a, b = list(map(int, input().split(" ")))
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph):
    queue = deque([1])
    visited = [1] 
    c = 0
    while queue: 
        n = queue.popleft()
        for nn in graph[n]:
            if nn not in visited:
                visited.append(nn)
                queue.append(nn)
                c += 1
    return c

print(bfs(graph))

            