
import string

def solution(msg):
    # 사전을 초기화한다.
    dict1 = {}
    # 사전에 A부터 Z까지 넣어준다. 색인 추가를 위해 인덱스에 1 추가한다. 
    for i in string.ascii_uppercase:
        dict1.update({i : string.ascii_uppercase.index(i)+1})

    
    idx = 1
    letter = msg[0]
    answer = []
    
    # idx가 len(msg)될 때까지 반복
    while idx < len(msg):
        # dict1 안에 없으면 밑의 과정을 수행한다.
        if letter + msg[idx] not in dict1:
            # answer에 색인값 추가
            answer.append(dict1[letter])
            # dict1에 새로운 단어 추가한다. 그리고 색인도 같이 추가해준다.
            dict1.update({letter + msg[idx]:len(dict1)+1})
            # letter는 다음 단어로 갱신한다.
            letter = msg[idx]
            idx += 1
            continue

        # 먄약 합쳐진 단어가 사전 안에 있을 경우
        else:
            # letter에 그 다음 단어를 추가해준다. 
            letter += msg[idx]
            # idx는 그대로 1 추가해준다.
            idx += 1
            
    answer.append(dict1[letter])
    
    return answer