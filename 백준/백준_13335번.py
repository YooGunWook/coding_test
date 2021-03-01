import collections

n, w, l = list(map(int, input().split(" ")))
trucks = collections.deque(list(map(int, input().split(" "))))


def solution(trucks):
    bridge = collections.deque([])
    times = collections.deque([])
    time = 0
    while trucks or bridge:
        time += 1
        if bridge:
            if times[0] + w == time:
                bridge.popleft()
                times.popleft()
        if trucks:
            if sum(bridge) + trucks[0] <= l:
                bridge.append(trucks.popleft())
                times.append(time)
    print(time)


solution(trucks)