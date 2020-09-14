def solution(n, a, b):
    # 우선 while 조건에 맞춰주기 위해 a가 더 클 경우 a와 b의 위치를 바꿔준다.
    answer = 0
    if a > b:
        a, b = b, a
    # 첫번째는 무조건 통과하기 때문에 1을 더해준다.
    answer += 1
    # 둘이 1과 2일 때 만나기 때문에 둘의 차이가 1이거나 a를 나눌 때 나머지가 1인 경우에 break. 
    while b-a != 1 or a % 2 != 1:
        # 첫번째 줄은 무조건 통과하기 때문에 1을 더하고 시작한다. 
        
        # a와 b 모두 동일한 조건으로 1이 남으면 2로 나눈 값에 1을 더해주고, 나머지가 없으면 2로 나눈 값으로 바꿔준다. 
        if a % 2 == 1:
            a = a//2 + a % 2
        elif a % 2 == 0:
            a = a//2
        if b %2 == 1:
            b = b//2 + b % 2
        elif b % 2 == 0:
            b = b//2
        
        answer += 1
    
    return answer