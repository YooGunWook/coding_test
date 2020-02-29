arrangement = '()(((()())(())()))(())'

def solution(arrangement):
    answer = 0 
    steel = [] # 막대기의 개수를 세기 위한 리스트
    arrangement = arrangement.replace('()','l') # 편의를 위해 l로 변환
    for i in arrangement: 
        if i == '(': # 시작하는 부분을 기준으로 answer에 1 추가
            steel.append('(')
            answer += 1
        elif i == ')': # 막대기가 끝나는 부분에 도달하면 뒤에부터 삭제
            steel.pop()
        else: # 레이저가 지나가는 부분 
            answer += len(stack) # 레이저가 한번 지나갈 때 stack의 길이만큼 증가.
    return answer
    
print(solution(arrangement))

