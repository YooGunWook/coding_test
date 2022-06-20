def solution(n, computers):
    answer = 0
    graph = {}
    for i_idx, computer in enumerate(computers):
        graph[i_idx] = []
        for j_idx, con in enumerate(computer):
            if i_idx == j_idx:
                continue
            if con == 1:
                graph[i_idx].append(j_idx)

    discovered = []
    for node in range(n):
        stack = [node]
        flag = False
        while stack:
            tmp_node = stack.pop()
            if tmp_node not in discovered:
                discovered.append(tmp_node)
                flag = True
                for new_node in graph[tmp_node]:
                    stack.append(new_node)
        if flag == True:
            answer += 1

    return answer


if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, computers))
