def solution(genres, plays):
    # 장르와 인덱스로 나눔
    di = {}
    for i in range(len(genres)):
        if di.get(genres[i]) == None:
            di[genres[i]] = {i:plays[i]}
        else:
            di[genres[i]][i] = plays[i]

    dic1 ={} # 값이 더 큰 순서대로 수록되기 때문에 합을 구함.
    for i, j in zip(di.values(), di):
        a = sum(i.values())
        dic1.update({j:a})
    dic1 = sorted(dic1.items(),key = (lambda x: x[1]), reverse = True) # 큰 순서대로 정렬


    genres_list = [] # 장르 순서대로
    for i in dic1:
        genres_list.append(i[0])


    play_lists = [] # play_lists 안에 수록곡 넣기
    for i in genres_list:
        a = sorted(di[i].items(), key = (lambda x : (x[1], -x[0])), reverse = True)
        # 수록곡은 장르별 최대 2개이기 때문에 2개 이상일 경우 앞에 2개만 넣어준다. 
        if len(a) > 2:
            for j in a[:2]:
                play_lists.append(j[0])
        # 2개 이하일 경우 다른 조건 없이 적용. 
        else:
            for j in a:
                play_lists.append(j[0])
    return play_lists #play_lists로 변환 