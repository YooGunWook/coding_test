# 우선 genre들의 play 횟수를 구한다
# 가장 높은 값을 우선으로 해서 순서를 구한다.
# 구한 값들을 list안에 넣어준다.

import collections


def solution(genres, plays):
    dictionary = {}
    for i, j in zip(genres, plays):
        if i not in dictionary:
            dictionary[i] = j
        else:
            dictionary[i] += j
    most_famous = collections.Counter(dictionary).most_common()

    genre_dictionary = {}
    for genre in most_famous:
        list_genre = {}
        for genre_check in range(0, len(genres)):
            if genres[genre_check] == genre[0]:
                list_genre.update({genre_check: plays[genre_check]})
        list_genre = collections.Counter(list_genre).most_common()
        genre_dictionary[genre[0]] = list_genre[0:2]

    final_list = []
    for play_list in genre_dictionary.values():
        for recommend in play_list:
            final_list.append(recommend[0])
    return final_list
