import collections

n, k = list(map(int, input().split(" ")))


def bfs(n, k):
    queue = collections.deque([(n, 0)])
    visited = collections.defaultdict(int)
    while queue:
        x, count = queue.popleft()
        m_x = x - 1
        p_x = x + 1
        mul_x = x * 2
        if x == k:
            print(count)
            break
        if visited[x] == 1:
            continue
        if 0 <= x <= 100001:
            visited[x] = 1
            queue.append((m_x, count + 1))
            queue.append((p_x, count + 1))
            queue.append((mul_x, count + 1))


bfs(n, k)