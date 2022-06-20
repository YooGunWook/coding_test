import heapq


def mix_scoville(val_1, val_2):
    return val_1 + (val_2 * 2)


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        if len(scoville) == 1:
            if scoville[0] >= K:
                break
            else:
                answer = -1
                break
        val = heapq.heappop(scoville)
        if val >= K:
            break
        else:
            val_2 = heapq.heappop(scoville)
            mix = mix_scoville(val, val_2)
            heapq.heappush(scoville, mix)
            answer += 1

    return answer


if __name__ == "__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    solution(scoville, K)
