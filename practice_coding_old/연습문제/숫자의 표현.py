def solution(n):
    answer = 0
    # 우선 count에 초기 숫자를 넣어준다.
    for i in range(1, n+1):
        count = i
        # 만약 n까지 오게 된다면 answer에 1 더해주고 break
        if count == n:
            answer += 1
            break
        # 1부터 시작해서 n에 도달할 때까지 더해준다.
        for j in range(i+1, n+1):
            count += j
            # 도달하면 answer에 1 더해주고 break
            if count == n:
                answer += 1
                break
            # 넘어가면 더해주지 않고 바로 break
            elif count > n:
                break
    return answer