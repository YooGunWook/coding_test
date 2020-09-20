import collections


def solution(bridge_length, weight, truck_weights):
    truck_weights = collections.deque(truck_weights)
    n = len(truck_weights)
    passed = []
    passing = collections.deque()
    passing_time = [0] * n
    j = 0
    i = 0

    while len(passed) != n:
        if len(truck_weights) > 0 and sum(passing) + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            passing.append(truck)
            j += 1

        passing_time[: j] = [passing_time[z] + 1 for z in range(0, j)]

        if passing_time[i] == bridge_length:
            truck = passing.popleft()
            passed.append(truck)
            i += 1

    return passing_time[0] + 1
