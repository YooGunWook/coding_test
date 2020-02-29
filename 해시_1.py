def solution(participant, completion):
    count_dict ={}
    for i in participant: # i participant가 count_dict 안에 있으면 +1, 없으면 i count_dict에 1을 넣어준다.  
        if i in count_dict:
            count_dict[i] = count_dict[i]+1
        else:
            count_dict[i] = 1
    for j in completion: # j completion이 count_dict 안에 있으면 1을 빼준다.
        if j in count_dict:
            count_dict[j] = count_dict[j]-1
    
    for j in count_dict:   # count_dict 값이 1이면 answer로 return
        if count_dict[j] == 1:
            a = j
    answer = a 
    return answer