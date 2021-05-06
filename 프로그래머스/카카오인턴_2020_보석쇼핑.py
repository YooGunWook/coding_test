import collections

def solution(gems):
    gem_list = set(gems) # 사야되는 보석들
    length = len(gem_list) # 사야되는 보석의 개수
    if length == 1: # 1이면 그냥 하나만 사면 됨
        return [1, 1]
    answer = [0, len(gems)] # 현재 정답의 길이
    start = 0 # 투 포인터
    end = 0 # 투 포인터
    dict_gems = collections.defaultdict(int) # 보석의 개수를 저장해주는 딕셔너리
    dict_gems[gems[0]] = 1 # 시작하는 부분의 보석 개수

    while start < len(gems) and end < len(gems):
        if len(dict_gems) == length: # 사야되는 보석을 전부 찾았을 때
            if end - start < answer[1] - answer[0]: # 길이 업데이트
                answer = [start, end]

            if gems[start] in dict_gems: # start가 늘어나기 때문에 빼준다
                dict_gems[gems[start]] -= 1

            if dict_gems[gems[start]] == 0: # 보석이 0이면 딕셔너리에서 빼준다
                del dict_gems[gems[start]]
            start += 1
        else:
            end += 1 # 원하는 보석을 전부 못 샀을 때 end를 1 늘려준다 
            if end == len(gems): # while문 break 시키기
                break
            dict_gems[gems[end]] += 1 # 살 수 있는 보석의 개수를 늘린다. 

    return [answer[0] + 1, answer[1] + 1]


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))