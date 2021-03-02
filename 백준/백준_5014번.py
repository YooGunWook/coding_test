import collections

f,s,g,u,d = list(map(int, input().split(' ')))

def bfs(s, g):
    queue = collections.deque([(s,0)])
    visited = [0] * (f + 1)
    visited[s] = 1
    while queue:
        floor, count = queue.popleft()
        visited[floor] = 1
        if s == g:
            if count < 1000000:
                return count
        if s< g:
            if s+u <=g:
                if visited[s+u] == 0:
                    queue.append((s+u, count + 1))
        elif s > g:
            if s-d >= g:
                if visited[s-d] == 0:
                    queue.append(s-d, count + 1)
            elif s-d<g:
                            
print(bfs(s,g))
