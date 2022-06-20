from collections import defaultdict, deque


def solution(tickets):
    graph = defaultdict(list)
    n = len(tickets)
    for ticket in tickets:
        a, b = ticket
        graph[a].append(b)
    for air in graph:
        graph[air].sort()
    queue = deque([["ICN", 0, []]])
    answer = []
    while queue:
        # print(stack)
        now, count, route = queue.popleft()
        for tar in graph[now]:
            if tar not in route:
                new_route = route + [tar]
                queue.append([tar, count + 1, new_route])

    return answer


if __name__ == "__main__":
    tickets = [
        ["ICN", "SFO"],
        ["ICN", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "ICN"],
        ["ATL", "SFO"],
    ]
    print(solution(tickets))
