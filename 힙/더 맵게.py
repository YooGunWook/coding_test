import heapq


def change_new_k(first, second):
    new_k = first + (second * 2)
    return new_k


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            answer = -1
            break
        second = heapq.heappop(scoville)
        new_scoville = change_new_k(first, second)
        heapq.heappush(scoville, new_scoville)
        answer += 1
    return answer
