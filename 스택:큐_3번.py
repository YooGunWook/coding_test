progresses = [93,30,55]
speeds = [1,30,5]
def solution(progresses, speeds):
    days = [] # 앞으로 몇번 더 해야 100%에 도달하는지 체크 
    answer = [] 
    for i, j in zip(progresses, speeds): # zip을 사용한 이유는 각 process별로 speed가 다르기 때문에 둘이 묶어서 계산.
        count = 0 # while 문을 통해 남은 기간을 체크. 
        while i < 100: # 100보다 커지는 순간 break
            i += j # 진행된 process에 speed만큼 100에 도달할 때까지 더해줌. 
            count += 1 # 진행될때마다 count에 1 추가
        days.append(count) # 남은 기간은 days에 append 시켜준다. 
        
    for i in range(1, len(days)): # 위에 사용한 예제에서는 필요 없을 수 있지만 다른 예제에서는 필요할 수 있고, 한칸만 작은게 아닌 갈수록 작을수 있기 때문에 같은 값으로 바꿔준다. 
        if days[i-1] > days[i]: # 어차피 그 이후에 프로젝트가 일찍 끝나더라도 첫번째 프로젝트가 끝나지 않으면 출시할 수 없음. 
            days[i] = days[i-1]
    
    count = 1
    for i in range(1, len(days)):
        if days[i-1] >= days[i]:
            count += 1 # 같거나 크면 1을 더해준다
        else:
            answer.append(count) # 그 외의 경우에서는 count를 append 시켜주고 
            count = 1 # count를 초기화한다.
    answer.append(count) # 최종 값을 append 해준다.
    return answer

print(solution(progresses,speeds))

