def find_appropriate(brown, red):
    # 우선 사용된 배열 수를 구한다.
    brown_red = brown + red
    # 1과 2의 경우 중간에 빨간 타일이 들어갈 수 없기 때문에 3부터 진행한다. 그리고 절반만 사용해서 for문을 최적화 시킨다. 
    for i in range(3,int(brown_red*0.5)+1):
        # j는 brown_red를 i로 나눴을 때 몫이다.
        j = brown_red // i
        # i * j를 곱해서 brown_red와 같은지 확인하고, 그 다음 i가 j보다 작으면 pass
        # 최종적으로 나온 i와 j에 -2씩 해서 red와 같아지면 그때 i와 j를 return 한다.
        if i*j == brown_red:
            if i < j:
                pass
            elif (i-2) * (j-2) == red:
                return i, j
    return i,j
    
def solution(brown, red):
    row, height = find_appropriate(brown, red)
    answer = []
    answer.append(row)
    answer.append(height)
    return answer