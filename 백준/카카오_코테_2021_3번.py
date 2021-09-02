from bisect import bisect_left
from itertools import combinations
import collections


def solution(info, query):
    answer = []
    infos = collections.defaultdict(list)

    for person in info:
        person = person.split(" ")
        person_key = person[:-1]
        person_val = int(person[-1])
        for i in range(5):
            for c in combinations(person_key, i):
                tmp_key = "".join(c)
                infos[tmp_key].append(person_val)
    for key in infos.keys():
        infos[key].sort()

    for que in query:
        que = que.split("and")
        que = [i.strip() for i in que]
        food, score = que[-1].split(" ")
        que.pop()
        que.append(food)
        while "-" in que:
            que.remove("-")
        tmp_q = "".join(que)
        if tmp_q in infos:
            scores = infos[tmp_q]
            if len(scores) > 0:
                mid = bisect_left(scores, int(score))
                answer.append(len(scores) - mid)
        else:
            answer.append(0)
    return answer
