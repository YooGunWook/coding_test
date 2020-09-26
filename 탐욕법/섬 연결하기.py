def solution(n,costs):
    visited = [0] * n
    costs.sort(key=lambda x: x[2])
    visited[0] = 1
    answer = 0
    while sum(visited) != n:
        for point in costs:
            start, end, cost = point
            if visited[start] or visited[end]:
                if visited[start] and visited[end]:
                    continue
                visited[start] = 1
                visited[end] = 1
                answer += cost
                continue
    return answer
