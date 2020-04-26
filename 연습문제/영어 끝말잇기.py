def solution(n, words):

    # 통과한 단어들을 넣어주는 list
    words_pass = []

    # answer에 들어가는 값들은 0부터 시작
    i = 0
    count = 0

    for j in range(0,len(words)):
        
        # 첫 순서는 무조건 통과하기 때문에 words_pass에 넣어주고 i에 1 더해준다. 
        if words_pass == []:
            words_pass.append(words[j])
            i += 1
            continue
            
        # 만약 i가 n에 도달하면 0으로 바꿔주고 count에 1 더해준다.     
        if i == n:
            i = 0
            count += 1
        
        # 우선 단어가 words_pass 안에 있는지 확인
        if words[j] not in words_pass:
            # word_pass 단어의 끝과 words 단어의 시작이 같은지 다른지 확인
            if words[j][0] == words_pass[-1][-1]:
                i += 1
                words_pass.append(words[j])
    
            # 만약 다를 경우 i와 count에 1 더해주고 break
            else:
                i += 1
                count += 1
                break
        # 만약 words_pass 안에 있던 단어면 i와 count에 1 더해주고 break
        else:
            i += 1
            count += 1
            break
            
    # 끝까지 아무런 break가 없다면 둘 다 0으로 초기화
    if len(words) == len(words_pass):
            i = 0
            count = 0
        
    answer = [i, count]

    return answer