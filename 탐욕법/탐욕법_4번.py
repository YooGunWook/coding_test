def solution(n, costs):
    answer = 0
    # cost가 작은 순서대로 정렬한다.
    costs.sort(key = lambda x:x[2])
    # 노드의 개수만큼 visited라는 list를 만들어준다.
    visited = [0] * n
    # 첫번째 노드부터 시작하기 때문에 1로 지정해준다.
    visited[0] = 1

    # visited의 합이 n에 도달할 때까지 반복
    # 왜냐하면 edge - 1 = node이기 때문이다.
    while sum(visited) != n:
        for i in costs:
            s,e,c = i

            # 우선 start 와 end 중 하나라도 값이 있을 경우
            if visited[s] or visited[e]:
                # 둘 다 값이 있을 경우 넘어간다.
                if visited[s] and visited[e]:
                    continue
                else:
                    # 그 외에는 start와 end에 1씩 지정해주고, answer에 c를 더해준 후 다음 값으로 넘어간다. 
                    # 예외 처리를 위해 start에도 1 지정해준다. 
                    visited[s] = 1
                    visited[e] = 1
                    answer += c
                    break
    return answer