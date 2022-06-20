import heapq


def solution(operations):
    heap = []
    for op in operations:
        op = op.split(" ")
        if op[0] == "I":
            heapq.heappush(heap, int(op[1]))
        elif op[0] == "D" and op[1] == "1":
            max_heap = []
            for val in heap:
                heapq.heappush(max_heap, -val)
            if not max_heap:
                continue
            heapq.heappop(max_heap)
            heap = []
            for val in max_heap:
                heapq.heappush(heap, -val)
        elif op[0] == "D" and op[1] == "-1":
            if not heap:
                continue
            heapq.heappop(heap)
    if not heap:
        return [0, 0]
    else:
        return [max(heap), min(heap)]


if __name__ == "__main__":
    operations = [
        "I -45",
        "I 653",
        "D 1",
        "I -642",
        "I 45",
        "I 97",
        "D 1",
        "D -1",
        "I 333",
    ]
    print(solution(operations))
