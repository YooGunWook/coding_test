import collections


class Solution:
    def dfs(self, visited, traced, graph, i):
        if i in traced:
            return False
        if i in visited:
            return True

        traced.add(i)
        # for loop를 할 때 빈 리스트일 경우 아예 작동하지 않음
        for end in graph[i]:
            if not self.dfs(visited, traced, graph, end):
                return False

        traced.remove(i)
        visited.add(i)
        return True

    def solution(self, prerequisites):
        traced = set()
        visited = set()
        graph = collections.defaultdict(list)

        for start, end in prerequisites:
            graph[start].append(end)

        for start in list(graph):
            if not self.dfs(visited, traced, graph, start):
                return False

        return True


if __name__ == "__main__":
    print(Solution().solution([[1, 0]]))
