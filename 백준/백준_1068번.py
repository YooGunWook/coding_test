import collections
import copy


def dfs(graph, k):
    stack = collections.deque([k])  # k값부터 탐색을 시작
    visited = []
    for key in graph:
        # 우선 각 node로 넘어갈 때 k가 있는지 확인. 없으면 제거
        if k in graph[key]:
            graph[key].remove(k)
            break
    # 그리고 tree 탐색을 통해 자식 노드들을 없애준다.
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            if v not in graph:
                continue
            while graph[v]:
                stack.append(graph[v].popleft())
    return graph


def check_leaf(graph, root):
    stack = collections.deque([root])  # root부터 탐색 시작
    visited = []
    count = 0  # 출력값
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            if not graph[v]:  # leaf 노드이면 count에 1 더해준다.
                count += 1
                continue
            for node in graph[v]:
                stack.append(node)
    return count


n = int(input())
tree = list(map(int, input().split(" ")))
graph = collections.defaultdict(collections.deque)
root = 0
for idx in range(len(tree)):
    if tree[idx] == -1:
        root = idx
        continue
    graph[tree[idx]].append(idx)
k = int(input())

if k == root:
    print(0)
else:
    graph = dfs(graph, k)
    print(check_leaf(graph, root))
