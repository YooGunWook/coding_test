# 우선 dict로 uid와 이름을 매칭 시킨다 -> dict가 여기선 매우 유용하다.
# 어차피 순서대로 나오기 때문에 이게 더 유용하다.
# 여기서 change와 나갔다 들어온 것을 반영해준다.
def change_result(new_record):
    dict1 = {}
    for i in range(0,len(new_record)):
        try:
            dict1.update({new_record[i][1]:new_record[i][2]})        
        except:
            continue
    return dict1
        

def solution(record):
    # 로그 정보 배열을 만든다.
    new_record = []
    answer = []
    
    # 로그 정보 배열을 넣어준다.
    for i in record:
        new_record.append(i.split(' '))
    
    # 위에서 만든 함수를 통해 최종 아이디를 만들어준다. 
    change = change_result(new_record)
    
    # for문을 통해 answer에 원하는 값을 넣어준다. 
    for i in range(0,len(new_record)):
        if new_record[i][0] == 'Enter':
            answer.append('{0}님이 들어왔습니다.'.format(change[new_record[i][1]]))
        if new_record[i][0] == 'Leave':
            answer.append('{0}님이 나갔습니다.'.format(change[new_record[i][1]]))
    return answer