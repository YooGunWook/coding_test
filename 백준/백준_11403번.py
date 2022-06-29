"""
플로이드 와샬 기반 풀이 
graph를 만들고 중간 지점이 존재할 경우 1로 채워준다. 
"""

n = int(input())
graph = []
for i in range(n):
    row = list(map(int, input().split(" ")))
    graph.append(row)


for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for row in graph:
    for col in row:
        print(col, end=" ")
    print()
