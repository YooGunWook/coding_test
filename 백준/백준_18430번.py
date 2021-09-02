n,m = list(map(int, input().split(' ')))
mat = []
for _ in range(n):
    row = list(map(int, input().split(' ')))
    mat.append(row)

dx, dy = [-1,1,0,0], [0,0,-1,1]    
boomerang = [(-1,1), (-1,-1), (1,-1), (1,1)]

def dfs(i, j, visited):
    for boom in boomerang:
        x,y = boom
        nx = i + x
        ny = j + y
        if visited[nx][ny] == 0 and 
    
    
    
def solution(mat):
    result = []
    for i in mat:
        for j in mat:
            visited = []
            for i in range(n):
                row = [0] * m
                visited.append(row)
            res = dfs(i,j, visited)
            result.append(res)
    return max(result)