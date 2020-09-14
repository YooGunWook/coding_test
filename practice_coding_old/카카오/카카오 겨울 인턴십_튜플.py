def dict_to_list(s):
    # list형태로 만들어주는 함수
    # list안에 list가 있는 형태로 만들어준다. 
    # 마지막에 길이 순서대로 정렬해준다. 
    s = s.split('},')
    list1 = []
    for i in s:
        i = i.replace('}','')
        i = i.replace('{','')
        list1.append(i)
    list3 = []
    for i in list1:
        a = i.split(",")
        list2 = []
        for j in a:
            list2.append(int(j))
        list3.append(list2)
    list3 = sorted(list3, key = lambda x: len(x) )
    return list3 

def solution(s):
    # tuple의 특성을 사용하자
    # 리스트별로 for문을 만든 후 그 안의 값을 check와 비교한다. 
    # check_list에 있으면 pass, 없으면 check와 answer에 각각 넣어준다.
    # 그리고 break
    s = dict_to_list(s)
    answer = []
    check = set()
    for i in range(0,len(s)):
        for each_value in s[i]:
            if each_value not in check:
                answer.append(each_value)
                check.add(each_value)
                break
    return answer