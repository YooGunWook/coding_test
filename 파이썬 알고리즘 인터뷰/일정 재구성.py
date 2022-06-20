import collections


class Solution:
    def __init__(self):
        self.result = []

    def dfs(self, graph, v, discovered=[]):
        discovered.append(v)
        for w in graph[v]:
            graph[v].pop(0)
            discovered = self.dfs(graph, w, discovered)
        self.result = discovered
        return self.result

    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)
        for aprt, deprt in sorted(tickets):
            graph[aprt].append(deprt)
        self.dfs(graph, "JFK")
        return self.result

    def stack_solution(self, tickets):
        graph = collections.defaultdict(list)
        for aprt, deprt in sorted(tickets):
            graph[aprt].append(deprt)
        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
        return route[::-1]
        