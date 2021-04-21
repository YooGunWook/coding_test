from itertools import combinations_with_replacement, permutations
import collections
import copy

n, m, d = list(map(int, input().split(" ")))
mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)
gung = [1, 1, 1] + ([0] * (n - 3))
gung_case = set(permutations(gung, m))
sol = collections.deque([])
for i in range(n):
    for j in range(m):
        if mat[i][j] == 1:
            sol.append((i, j))


def bfs(mat, sol, d, gungs, n):
    gungs_list = []
    for idx in gungs:
        if gungs[idx] == 1:
            gungs_list.append((n, idx))
    target_point = []
    for i in range(n):
        for j in range(m):
            for gung in gungs_list:
                if abs(gung[0] - i) + abs(gung[1] - j) <= d:
                    target_point.append((i,j))
    
    
    while sol:
        
            
            
