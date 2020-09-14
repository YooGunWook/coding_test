# BFS 구현
def find_connection(computers,visited,n, i):
    queue = [i]
    
    # 큐가 사라질 때까지 반복
    while queue:
        node = queue.pop(0)
        visited[node] = True
        # visited가 False라는 조건을 걸어서 방문하지 않았을 때나 노드가 1인 경우 queue에 더해준다.
        for k in range(n):
            if visited[k] == False and computers[node][k] == 1:
                queue.append(k)
    
def solution(n,computers):
    visited = [False for i in range(n)]
    answer = 0
    # n번만큼 for문을 돌린다. 
    for i in range(n):
        # visited가 False면 반복해준다. 
        # True면 다음으로 넘어간다.
        # False일 때마다 1씩 더해준다. 
        if visited[i] == False:
            find_connection(computers,visited,n,i)
            answer += 1

    return answer