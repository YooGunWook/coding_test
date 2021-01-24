import heapq
from collections import deque


def solution(tree_list):
    if not tree_list:
        return 0
    queue = deque(tree_list)
    tree = deque([])
    depth = 1
    node = queue.popleft()
    tree.append([node])
    while queue:
        tmp_depth = []
        depth += 1
        while len(tmp_depth) < depth - 1:
            if len(queue) == 0:
                break
            if len(queue) == 1:
                node1 = queue.popleft()
                tmp_depth.append([node1])
                break
            node1 = queue.popleft()
            node2 = queue.popleft()
            tmp_depth.append([node1, node2])

        tree.append(tmp_depth)

    print(tree)
    return depth


if __name__ == "__main__":
    print(
        solution(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        )
    )
