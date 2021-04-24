import collections
import itertools
import copy

n, m, h = list(map(int, input().split(" ")))
graph = collections.defaultdict(collections.deque)
al_connect = []
for _ in range(m):
    a, b = list(map(int, input().split(" ")))
    graph[b].append((b + 1, a))
    graph[b + 1].append((b, a))
    al_connect.append((b, a))

possible_connect = []
for row in range(1, h + 1):
    for col in range(1, n):
        if (
            (col, row) not in al_connect
            and (col + 1, row) not in al_connect
            and (col - 1, row) not in al_connect
        ):
            possible_connect.append((col, row))


def dfs(graph, i):
    stack = [graph[i][0]]
    visited = []
    while stack:
        col, row = stack.pop()
        if (col, row) not in visited:
            visited.append((col, row))
            for new_col in graph[col]:
                if new_col[1] > row:
                    # col + 1 == new_col[0] or col - 1 == new_col[1]
                    stack.append(new_col)
                    break
    return visited[-1][0]


if m == 0:
    print(0)
elif not possible_connect:
    print(-1)
else:
    idx = 1
    while True:

        candidates = itertools.combinations(possible_connect, idx)

        for candidate in candidates:
            flag = False
            tmp_graph = copy.deepcopy(graph)

            for cand in candidate:
                b, a = cand
                tmp_graph[b].append((b + 1, a))
                tmp_graph[b + 1].append((b, a))

            for key in tmp_graph:
                tmp_graph[key] = sorted(tmp_graph[key], key=lambda x: x[1])

            for key in tmp_graph:
                if key != dfs(tmp_graph, key):
                    flag = True
                    break

            if flag == True:
                continue
            elif flag == False:
                break

        if flag == True:
            idx += 1
        elif flag == False:
            break

        if idx > 3:
            idx = -1
            break

    print(idx)
