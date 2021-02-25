import collections

n, m = list(map(int, input().split(" ")))
miro = []
for _ in range(n):
    miro.append(list(map(int, input())))

dx, dy = [-1, 1, 0, 0], [0,0, -1, 1]

visited = [[0] * m for _ in range(n)]
queue = collections.deque([(0,0)])
visited[0][0] = 1

while queue:
    print(queue)
    x,y = queue.popleft()
    
    if x == n -1 and y == m-1:
        print(visited[x][y])
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and miro[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))