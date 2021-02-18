# N, T = map(int, input().split(" "))


def binary_search(T, start, interval, count):
    if T == start:
        return 0

    bus_info = [start]
    for _ in range(count - 1):
        start += interval
        bus_info.append(start)

    tmp_value = 1000000001

    while True:
        mid = len(bus_info) // 2

        if mid == 0:
            if bus_info[0] - T < 0:
                break
            tmp_value = min(tmp_value, bus_info[0] - T)
            break

        left, right = bus_info[:mid], bus_info[mid:]

        if left[-1] < T:
            bus_info = right
            continue

        if abs(left[-1] - T) >= abs(right[0] - T):
            bus_info = right
            tmp_value = min(tmp_value, abs(right[0] - T))
            continue

        elif abs(left[-1] - T) < abs(right[0] - T):
            bus_info = left
            tmp_value = min(tmp_value, abs(left[-1] - T))
            continue

    if tmp_value == 1000000001:
        return -1

    return tmp_value


if __name__ == "__main__":
    print(binary_search(352, 315, 15, 3))