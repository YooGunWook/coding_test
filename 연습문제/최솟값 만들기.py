def solution(A,B):
    answer = []
    # 우선 최소값을 구하기 위해서는 A는 오름차순, B는 내림차순으로 정렬해준다. 
    A = sorted(A)
    B = sorted(B, reverse = True)
    # 0부터 시작하는 누적합이기 때문에 i*j를 answer에 append 해준다.
    for i, j in zip(A,B):
        print(i,j)
        answer.append(i*j)
    # 전체를 합해준다. 
    answer = sum(answer)
    return answer