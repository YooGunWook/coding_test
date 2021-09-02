day = 0
while True:
    day += 1
    p = int(input())
    if p == 0:
        break
    party_list = []
    for _ in range(p):
        party_list.append(tuple(map(int, input().strip().split(" "))))
    party_list.sort()

    count = 1
    time = party_list[0][0]
    if party_list[0][0] == party_list[0][1]:
        minute = "00"
    else:
        minute = "50"
    now = int(str(time) + str(minute))
    for party in party_list[1:]:
        print(now)
        end_time = int(str(party[1]) + "00")
        start_time = int(str(party[0]) + "00")
        if start_time == end_time and start_time == now:
            count += 1
            continue
        if now >= end_time:
            continue
        now = max(start_time, now)
        if now < end_time:
            now += 50
            count += 1

    print(f"On day {day} Emma can attend as many as {count} parties.")