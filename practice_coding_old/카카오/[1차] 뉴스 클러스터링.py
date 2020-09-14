from collections import Counter
def solution(str1, str2):
    # 우선 str들을 소문자로 바꿔준다
    str1 = str1.lower()
    str2 = str2.lower()
    # 조합을 담을 리스트 생성
    list_str1 = []
    list_str2 = []
    
    # len -1 을 해서 여기서 원하는 규칙대로 단어를 만듦. 
    for i in range(0,len(str1)-1):
        
        i = str1[i:i+2]

        # isalpha가 false면 그대로 넘어간다. 
        if i.isalpha() == False:
            continue
        else:
            list_str1.append(i)
        
    # str2에도 똑같은 방식대로 해준다. 
    for i in range(0,len(str2)-1):
        i = str2[i:i+2]

        if i.isalpha() == False:
            continue
        else:
            list_str2.append(i)
    
    # collections에 있는 Counter 함수를 쓰게 되면 매우 편하게 계산할 수 있게 된다. 
    list_str1_count = Counter(list_str1)
    list_str2_count = Counter(list_str2)
    
    # Counter후에 교집합과 합집합을 구하게 되면 데이터에 손실이 일어나지 않게 된다. 
    inter =  list_str1_count & list_str2_count
    union =  list_str1_count | list_str2_count
    
    # value의 합을 구해준다.
    inter_value = sum(list(inter.values()))
    union_value = sum(list(union.values())) 
    
    
    # try, except를 통해 계산을 해준다. 
    try:
        answer = int((inter_value/union_value) * 65536)
    except ZeroDivisionError:
        
        answer = 1 * 65536
    
    return answer