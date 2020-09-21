def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    # 각 항목별로 count 하기 위한 변수 추가
    a = 0
    b = 0
    c = 0
    # 정답
    answer = []
    
    # while문을 통해 answers와 수포자들의 answer 길이를 맞춰준다.
    # (이건 좀 무식한 방식이고 for문으로 순환주기 나눠주면 좀 더 깔끔한 코딩이 나옴.)
    i = 0
    while len(s1) < len(answers):
        s1.append(s1[i])
        i += 1
        if i == len(s1):
            i = 0 
        
    i = 0
    while len(s2) < len(answers):
        s2.append(s2[i])
        i += 1
        if i == len(s2):
            i = 0 
        
    i = 0
    while len(s3) < len(answers):
        s3.append(s3[i])
        i += 1
        if i == len(s3):
            i = 0 
    
    # 각 수포자별로 맞춘 점수를 count 했음. 
    answer_count = []
    for i, j in zip(answers,s1):
        if i == j:
            a += 1
    answer_count.append(a)
    
    for i, j in zip(answers,s2):
        if i == j:
            b += 1
    answer_count.append(b)
    
    for i, j in zip(answers,s3):
        if i == j:
            c += 1
    answer_count.append(c)

    # 가장 많이 맞춘 수포자를 answer에 append 해준다. 
    for i in range(len(answer_count)):
        if answer_count[i] == max(answer_count):
            answer.append(i + 1)
    
    return answer