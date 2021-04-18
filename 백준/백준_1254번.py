from itertools import permutations
from itertools import combinations

s = str(input())


def my_solution(s):
    # 처음에 같으면 해당 문자열을 그대로 길이로 출력
    # 이렇게 풀면 시간 초과
    if s == s[::-1]:
        return len(s)
    # window를 기반으로 뒤에 붙여서 탐색
    for window in range(1, len(s)):
        tmp_window = window
        already_done = []  # 이미 한 애들은 따로 보지 않는다.
        for idx in range(0, len(s)):
            # 각 window에 들어간 문자만큼 경우의 수를 만들어준다.
            target_word = list(permutations(s[idx:tmp_window], window))
            tmp_window += 1  # 1개씩 더해서 다음 애들을 볼 수 있게 한다.
            for word in target_word:
                target = "".join(word)
                if target in already_done:
                    continue
                # target과 원래 단어를 합쳐서 팰린드롬 여부 확인
                tmp_word = s + target
                if tmp_word == tmp_word[::-1]:
                    return len(tmp_word)
                already_done.append(target)


def good_solution(s):
    # 부분 문자열이 팰린드롬이 되면 본 개수만큼 더해서 출력시킨다.
    for i in range(len(s)):
        if s[i:] == s[i:][::-1]:
            return len(s) + i


print(good_solution(s))