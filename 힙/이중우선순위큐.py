import heapq


def solution(operations):
    heap = []

    for operator in operations:

        if 'I' in operator:
            operator = operator.split(' ')
            heapq.heappush(heap, int(operator[1]))

        elif heap:
            if 'D -1' in operator:
                heapq.heapify(heap)
                heapq.heappop(heap)
            elif 'D 1' in operator:
                heapq._heapify_max(heap)
                heapq._heappop_max(heap)
    if not heap:
        return [0, 0]

    return [max(heap), min(heap)]