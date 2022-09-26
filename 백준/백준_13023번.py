from collections import defaultdict

n, m = list(map(int, input().split(" ")))


graph = defaultdict(list)
for _ in range(m):
    a, b = list(map(int, input().split(" ")))
    graph[a].append(b)
    
stack = []
for key in graph:
    stack = [key]
    visited = [key]
    while stack:
        
