import heapq
import collections


def solution(n, start, end, roads, traps):
    graph = {i: {} for i in range(1, n + 1)}
    for i in roads:
        graph[i[0]][i[1]] = i[2]
    dist = {i: float("inf") for i in graph}
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cur_cost, cur_node = heapq.heappop(queue)

        if cur_cost == end:
            break

        if dist[cur_node] < cur_cost:
            continue

        for new_node, new_cost in graph[cur_node].items():
            cost = cur_cost + new_cost
            dist[new_node] = cost
            heapq.heappush(queue, (cost, new_node))

            if new_node in traps:
                trap = new_node
                new_graph = {i: {} for i in range(1, n + 1)}
                for node in new_graph:
                    tmp_graph = graph[node]
                    if node == trap:
                        for tmp_node in tmp_graph:
                            new_graph[tmp_node][node] = graph[node][tmp_node]

                    else:
                        for tmp_node in tmp_graph:
                            if tmp_node == trap:
                                new_graph[tmp_node][node] = graph[node][tmp_node]
                            else:
                                new_graph[node][tmp_node] = graph[node][tmp_node]

                graph = new_graph

    answer = dist[end]
    return answer


############ 정답 풀이 ####################


def solution(n, start, end, roads, traps):
    start -= 1
    end -= 1
    graph = collections.defaultdict(list) # 각 노드별 가는 길 저장
    trap_dict = {trap - 1: idx for idx, trap in enumerate(traps)} # value: 비트 마스크에서 각 함정을 뜻하는 자리수로 사용 함정의 순서
    queue = [] 
    isVisit = [[False] * n for _ in range(1 << len(traps))] # 2^n만큼 생성

    for road in roads:
        start_i, end_i, cost = road
        graph[start_i - 1].append([end_i - 1, cost, 0])
        graph[end_i - 1].append([start_i - 1, cost, 1])

    heapq.heappush(queue, (0, start, 0))

    while queue:
        cur_time, cur_node, state = heapq.heappop(queue)
        if cur_node == end:
            break
        if isVisit[state][cur_node] == True:
            continue
        isVisit[state][cur_node] = True

        for next_node, next_cost, road_type in graph[cur_node]:
            next_state = state
            cur_isTrap = 1 if cur_node in trap_dict else 0
            next_isTrap = 1 if next_node in trap_dict else 0

            if cur_isTrap == 0 and next_isTrap == 0:
                if road_type == 1:
                    continue
            elif cur_isTrap + next_isTrap == 1:
                node_i = cur_node if cur_isTrap == 1 else next_node
                isTrapOn = (state & (1 << trap_dict[node_i])) >> trap_dict[node_i]
                if isTrapOn != road_type:
                    continue
            else:
                isTrapOn = (state & (1 << trap_dict[cur_node])) >> trap_dict[cur_node]
                n_isTrapOn = (state & (1 << trap_dict[next_node])) >> trap_dict[
                    next_node
                ]
                if (isTrapOn ^ n_isTrapOn) != road_type:
                    continue
            if next_isTrap == 1:
                next_state = state ^ (1 << trap_dict[next_node])

            heapq.heappush(queue, (cur_time + next_cost, next_node, next_state))

    return cur_time


roads = [[1, 2, 2], [3, 2, 3]]
print(solution(3, 1, 3, roads, [2]))
