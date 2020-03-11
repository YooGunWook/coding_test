def solution(stock, dates, supplies, k):
    answer = 0
    heap = [] # 우선순위 큐를 만들어준다. 
    idx = 0 # 시작지점을 0으로 설정해준다.
    while stock < k:
        for i in range(idx, len(dates)): 
            if stock < dates[i]: # stock이 dates[i]보다 작으면 break해준다. 
                break
            heapq.heappush(heap,-supplies[i]) # 우선순위 큐를 만들어준다. 
            idx = i+1 # 시작지점을 +1 옮겨준다. 
        stock += (heapq.heappop(heap)*-1) # stock에 큰 숫자만큼 더해준다. 
        answer += 1 # 더해준만큼 1을 더해준다. 
        # 이 과정을 반복하다보면 k보다 커지는 경우가 생기는데 그때 break가 일어날 것이다. 

    return answer