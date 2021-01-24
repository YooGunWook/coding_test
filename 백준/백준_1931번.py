import collections


def solution(n, timeline) -> int:
    cnt = 1
    end_time = timeline[0][1]
    for discuss in range(1, n):
        if timeline[discuss][0] >= end_time:
            cnt += 1
            end_time = timeline[discuss][1]
    return cnt


if __name__ == "__main__":
    timeline = [
        (1, 4),
        (3, 5),
        (0, 6),
        (5, 7),
        (3, 8),
        (5, 9),
        (6, 10),
        (8, 11),
        (8, 12),
        (2, 13),
        (12, 14),
    ]
    timeline.sort(key=lambda x: (x[1], x[0]))
    print(solution(11, timeline))