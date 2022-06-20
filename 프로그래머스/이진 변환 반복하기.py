def solution(s):
    zero_count = 0
    rem_count = 0
    while s != "1":
        tmp_count = s.count("0")
        zero_count += tmp_count
        s = s.replace("0", "")
        s = format(int(len(s)), "b")
        rem_count += 1
    answer = [rem_count, zero_count]
    return answer


print(solution("110010101001"))