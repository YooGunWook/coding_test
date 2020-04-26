# n진수 만드는 함수
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def solution(n, t, m, p):
    # player는 1부터 시작하기 때문에 1로 지정
    count_player = 1
    # turn을 하나씩 count
    turn = 0
    # 우선 경우의 수를 모두 여기에 넣는다.
    answer = ''
    # n진수로 변환한 값을 넣어준다.
    list_number = []
    # 실제 정답을 여기에 넣는다.
    real_answer = ''

    # n진수로 변환한 값을 넣는다. 
    # 길이는 t*m만큼
    for i in range(0, t*m):
        value = convert(i,n)
        list_number.append(value)
    
    # 가짜 정답을 만든다. 
    for i in list_number:
        for j in range(0,len(i)):
            answer += i[j]

            
    while turn < t:
        for i in range(0,len(answer)):
            # m과 p가 같은 경우가 있기 때문에 if문을 활용한다. 
            # turn에 1을 더해주고 count_player는 초기화
            if count_player == m:
                if count_player == p:
                    real_answer += answer[i]
                    count_player = 1
                    turn += 1
                else:
                    count_player = 1
                    turn += 1
            # m과 p가 같지 않은 경우
            # count_player를 1씩 더해주고, p와 같아지면 real_answer에 넣어준다. 
            else:
                if count_player == p:
                    real_answer += answer[i]
                    count_player += 1
                else:
                    count_player += 1
            
            # while문이 잘 안먹혀서 씀. turn이 t와 같아지면 break
            if turn == t:
                break
            
    
    return real_answer