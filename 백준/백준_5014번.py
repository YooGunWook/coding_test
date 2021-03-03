import collections

f,s,g,u,d = list(map(int, input().split(' ')))

def bfs(s, g):
    if s < g and u == 0:
        return 'use the stairs'
    if s > g and d == 0:
        return 'use the stairs'
    if s == g:
        return 0
    queue = collections.deque([(s,0)])
    visited = collections.defaultdict(int)
    visited[s] = 1
    floor_d = 0
    floor_u = 0
    while queue:
        
        floor, count = queue.popleft()
        
        if floor == 1 or d == 0:
            floor_u = floor + u 
            visited[floor] = 1
            if 1 <= floor_u <= f and visited[floor_u] == 0:
                if floor_u == g:
                    count += 1
                    return count
                count += 1
                queue.append((floor_u, count))
                visited[floor_u] = 1
                
        elif floor == f or u == 0:
            floor_d = floor - d
            if 1 <= floor_d <= f and visited[floor_d] == 0:
                if floor_d == g:
                    count += 1
                    return count
                count += 1
                queue.append((floor_d, count))
                visited[floor_d] = 1
                
        elif u != 0 and d != 0:
            floor_u = floor + u
            floor_d = floor - d 
            if 1 <= floor_u <= f and 1 <= floor_d <= f:
                if floor_u == g or floor_d == g:
                    count += 1
                    return count
                count += 1
                if visited[floor_u] == 0 and visited[floor_d] == 1:
                    queue.append((floor_u, count))
                    visited[floor_u] = 1
                    continue
                elif visited[floor_d]== 0 and visited[floor_u] == 1:
                    queue.append((floor_d, count))
                    visited[floor_d] = 1
                    continue
                elif visited[floor_d] == 1 and visited[floor_u] == 1:
                    continue
                queue.append((floor_u, count))
                queue.append((floor_d, count))
                visited[floor_u] = 1
                visited[floor_d] = 1
    return 'use the stairs'
print(bfs(s,g))

