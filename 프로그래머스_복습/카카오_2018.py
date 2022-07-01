from collections import deque


def get_minute(time):
    hour, minute = time.split(":")
    hour = int(hour) * 60
    minute = int(minute)
    return hour + minute


def time_maker(start_time):
    if start_time // 60 < 10:
        hour = "0" + str(start_time // 60)
    else:
        hour = str(start_time // 60)
    if start_time % 60 < 10:
        minute = "0" + str(start_time % 60)
    else:
        minute = str(start_time % 60)
    return hour, minute


def solution(n, t, m, timetable):
    n_timetable = []
    answer = ""
    for time in timetable:
        n_timetable.append(get_minute(time))
    n_timetable = sorted(n_timetable)
    start_time = 9 * 60
    idx = 0
    for bus in range(n):
        cnt = 0
        for _ in range(m):
            if cnt < m and idx < len(n_timetable) and n_timetable[idx] <= start_time:
                idx += 1
                cnt += 1
        if cnt < m:
            ans_time = start_time
        else:
            ans_time = n_timetable[idx - 1] - 1
        start_time += t

    answer = time_maker(ans_time)
    answer = answer[0] + ":" + answer[1]
    return answer
