import collections
# collections의 Counter 활용
# 각각의 값들을 Counter를 통해 구한 후 most_common(1)로 최종 값 도출


def solution(participant, completion):
    participant_dictionary = collections.Counter(participant)
    for complete in completion:
        if complete in participant_dictionary:
            participant_dictionary[complete] -= 1
    return participant_dictionary.most_common(1)[0][0]