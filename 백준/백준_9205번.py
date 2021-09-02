import collections

t = int(input())


def man_distance(x, y, nx, ny):
    return abs(x - nx) + abs(y - ny)


def bfs(home_x, home_y):
    queue = collections.deque([(home_x, home_y, 20)])
    visited = collections.defaultdict(int)
    visited[(home_x, home_y, 20)] = 1
    while queue:
        print(queue)
        x, y, count = queue.popleft()
        if x == fes_x and y == fes_y:
            print("happy")
            return
        for nx, ny in store:
            if visited[(nx, ny, 20)] == 0:
                l1 = man_distance(x, y, nx, ny)
                if count * 50 >= l1:
                    print(l1)
                    queue.append((nx, ny, 20))
                    visited[(nx, ny, 20)] = 1
    print("sad")
    return


for _ in range(t):
    n = int(input())
    home_x, home_y = list(map(int, input().split(" ")))
    store = []
    for _ in range(n):
        store.append(list(map(int, input().split(" "))))
    fes_x, fes_y = list(map(int, input().split(" ")))
    store.append([fes_x, fes_y])
    bfs(home_x, home_y)