import heapq


def solution(jobs):
    n = len(jobs)
    now, answer, start = 0, 0, -1
    i = 0
    heap = []
    while i < n:
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        if len(heap) > 0:
            tmp_job = heapq.heappop(heap)
            start = now
            now += tmp_job[0]
            answer += now - tmp_job[1]
            i += 1
        else:
            now += 1

    return answer // n


if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [2, 6]]
    print(solution(jobs))
