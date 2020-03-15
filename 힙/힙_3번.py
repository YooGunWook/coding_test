def solution(jobs):
    pq = []
    time = 0
    # 끝난기록이 없기 때문에 -1을 넣어준다. 
    end = -1
    answer = 0
    # 처리한 프로세스 개수
    count = 0
    # jobs의 길이
    n = len(jobs)
    while count < n:
        for i in jobs:
            # i[0]은 요청 시간, i[1] 프로세스가 끝날때까지 걸리는 시간
            if end < i[0] <= time:
                # queue 안에서 얼마나 기다렸는지 계산
                answer += (time-i[0])
                heapq.heappush(pq, i[1])
        if len(pq) > 0:
            # 가장 빨리 끝나는 프로세스가 끝날 때까지 큐에 있는 프로세스는 기다려야 하므로 값을 추가한다. 
            # C가 수행되는 동안 B가 이미 들어와 있어서 같이 대기를 하는 것이다. 따라서 C의 수행시간 6ms만큼 B가 대기하고 있는
            # 것이다. 그래서 6*2 = 12ms만큼 더해야하는 것이다. 
            answer += len(pq) * pq[0]
            end = time
            time += heapq.heappop(pq)
            count += 1
        else:
            time += 1
    return (int(answer/n))
