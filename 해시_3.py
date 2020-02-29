# collections 안에 있는 Counter 함수를 부름 
from collections import Counter


def solution(clothes):
    answer = 1
    # Counter 함수를 쓰면 clothes에 있는 값을 count 해줌. 
    c = Counter([x[1] for x in clothes])

    # c에 할당된 값들을 answer에 i+1만큼 곱해준다. 
    for i in c.values():
        answer *= i+1
    
    # 최종 결과로 나타낼때는 -1을 해줌. 
    answer -= 1
    return answer