from itertools import combinations

def solution(relation):
    # 우선 row와 col의 개수를 구한다.
    n_row = len(relation)
    n_col = len(relation[0])
    # 유의성에 통과한 조합을 final에 넣는다.
    final = []
    # 조합을 찾는다.
    candidate_list = []
    
    # combination을 써서 모든 조합을 찾는다
    # 여기서는 최대 8개이기 때문에 사용해도 됨.
    for i in range(1,n_col+1):
        combination_l = combinations(range(n_col), i)
        candidate_list.extend(combination_l)

    # 유의성 검정
    for i in candidate_list:
        final_tmp = []
        for j in range(0, n_row):
            temp_list = []
            for k in i:
                # 우선 모든 조합의 값을 넣어준다.
                temp_list.append(relation[j][k])
            final_tmp.append(tuple(temp_list))
        # 유의성에 통과하기 위해서는 row값과 조합을 통해 만들어진 값의 길이가 같아야한다.     
        if len(relation) == len(set(final_tmp)):
            final.append(i)

    # 최소성 검정
    final_set = set(final)
    for i in range(0,len(final) - 1):
        for j in range(i+1, len(final)):
            # 만약 final[i]와 final[j]의 교집합이 final[i]와 같다면 최소성을 만족하지 못하는 것이다.
            # set의 특징이 있다면 set안에 없는 값을 discard해도 에러가 나지 않는다.  
            if set(final[i]) == set(final[i]) & set(final[j]):
                final_set.discard(final[j])
    
    
    answer = len(final_set)
    return answer