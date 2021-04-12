n, m = list(map(int, input().split(' ')))
r,c,d = list(map(int, input().split(' ')))
mat = []
visited = []
for _ in range(n):
    row = list(map(int, input().split(' ')))
    mat.append(row)
    visited.append([0] * m)
    
def bfs(r,c, mat, visited):
    queue = [(r,c)]
    