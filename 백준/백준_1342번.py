from collections import Counter

s = list(input())
len_s = len(s)
s_count = Counter(s)


def back_traking(now, length):  # 백트래킹 기반 풀이
    if length == len_s:
        return 1
    answer = 0
    for key in s_count:
        if s_count[key] == 0:
            continue
        if key == now:
            continue
        s_count[key] -= 1
        answer += back_traking(key, length + 1)
        s_count[key] += 1
    return answer


print(back_traking("", 0))
