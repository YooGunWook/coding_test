import collections


import collections


def solution(gems):
    gem_list = set(gems)
    length = len(gem_list)
    if length == 1:
        return [1, 1]
    answer = [0, len(gems)]
    start = 0
    end = 0
    dict_gems = collections.defaultdict(int)
    dict_gems[gems[0]] = 1

    while start < len(gems) and end < len(gems):
        if len(dict_gems) == length:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]

            if gems[start] in dict_gems:
                dict_gems[gems[start]] -= 1

            if dict_gems[gems[start]] == 0:
                del dict_gems[gems[start]]
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            dict_gems[gems[end]] += 1

    return [answer[0] + 1, answer[1] + 1]


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))