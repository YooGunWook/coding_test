# 정규식을 사용해서 숫자와 그 외 문자열을 분리시킬 예정
import re
def solution(files):

    answer = []
    # 정규식으로 분리
    temp =  [re.split(r"([0-9]+)", s) for s in files]

    # sort 함수를 이용해서 두가지에 대해서 정렬할 수 있게 함. 
    # 우선순위를 앞에다 둠
    
    dict_sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    
    # 합쳐줌
    for i in range(0,len(dict_sort)):
        a = ''.join(dict_sort[i])
        answer.append(a)


    return answer