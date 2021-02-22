day = 0
while True:
    day += 1
    p = int(input())
    if p == 0:
        break
    party_list = []
    for _ in range(p):
        party_list.append(tuple(map(int, input().strip().split(" "))))
    party_list.sort(key=lambda x: x[0])

    count = 1
    time = party_list[0][0]
    minute = 50
    now = int(str(time) + str(minute))
    for party in party_list[1:]:
        end_time = int(str(party[1]) + "00")
        start_time = int(str(party[0]) + "00")
        if now >= end_time:
            continue
        if start_time > now:
            while start_time > now:
                now += 50
        if now <= end_time:
            if party_list[0] == party_list[1]:
                count += 1
                continue
            now += 50
            count += 1

    print(f"On day {day} Emma can attend as many as {count} parties.")
