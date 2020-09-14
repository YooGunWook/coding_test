import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 우선 이 데이터를 heap 형태로 만들어준다.
    while scoville:
        a = heapq.heappop(scoville) # heap으로 처리하게 되면 작은 숫자가 어디에 있어도 가장 작은 값을 먼저 빼준다. 
        if a >= K : # 순서대로 뽑히기 때문에 만약 제일 작은 값이 K보다 크거나 같으면 break 해준다. 
            break
        if len(scoville) == 0: # scoville에 남은 값이 없으면 그 데이터 안에 K보다 크게 할 수 있는 값이 없다는 의미이기 때문에 -1을 반환한다. 
            answer = -1
            return answer
        b = heapq.heappop(scoville) # 두번째로 덜 매운 값을 뽑아준다. 
        heapq.heappush(scoville,a+(b*2)) # list안에 이 데이터 값을 넣어준다.
        answer += 1
        
    return answer