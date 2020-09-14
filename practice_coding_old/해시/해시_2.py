def solution(phone_book):

    phone_book = sorted(phone_book, key = len) #phone_book을 sort 시켜줌. 
    
    list1 = [] # list1이라는 empty 리스트 생성
    
    # for문에 넣어주기 위해 a에 phone_book 할당
    a = phone_book
    
    # 접두에 들어갈 폰 번호를 따로 빼준다. 
    front = phone_book[0]
    # 접두에 들어간 폰 번호만 제외
    del a[:1]

    # startswith이라는 모듈을 사용해서 a에 있는 번호들의 앞이 front와 같으면 list1에 False를 넣어준다. 그 외에는 True
    for j in a:
        if j.startswith(front):
            list1.append(False)
        else: 
            list1.append(True)
    
    # False가 list1 안에 있으면 False로 return, 그 외에는 True
    if False in list1:
        a = False
    else:
        a = True
    return a