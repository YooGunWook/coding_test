from collections import deque
class GraphAlgorithm:
    def dfs_graph(self, v, discovered=[]):
        # 스택과 재귀로 구현 가능. 재귀로 진행
        graph = {
            1: [2, 3, 4],
            2: [5],
            3: [5],
            4: [],
            5: [6, 7],
            6: [],
            7: [3],
        }
        discovered.append(v)
        for w in graph[v]:
            if not w in discovered:
                discovered = self.dfs_graph(w, discovered)
        return discovered

    def dfs_stack(self, start_v):
        graph = {
            1: [2, 3, 4],
            2: [5],
            3: [5],
            4: [],
            5: [6, 7],
            6: [],
            7: [3],
        }
        discovered = []
        stack = [start_v]
        while stack:
            v = stack.pop()
            if v not in discovered:
                discovered.append(v)
                for w in graph[v]:
                    stack.append(w)
        return discovered

    def bfs_queue(self, start_v):
        graph = {
            1: [2, 3, 4],
            2: [5],
            3: [5],
            4: [],
            5: [6, 7],
            6: [],
            7: [3],
        }
        discovered = deque([start_v])
        queue = deque([start_v])
        while queue:
            v = queue.popleft()
            for w in graph[v]:
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)
        return discovered


if __name__ == "__main__":
    print(f"recursive dfs :{GraphAlgorithm().dfs_graph(1)}")
    print(f"stack dfs :{GraphAlgorithm().dfs_stack(1)}")
    print(f"queue bfs :{GraphAlgorithm().bfs_queue(1)}")
