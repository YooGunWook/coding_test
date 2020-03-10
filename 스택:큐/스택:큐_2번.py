bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights[::-1] # 원래 리스트를 뒤집어서 좀 더 효율적으로 알고리즘을 실행시킴
    passed = [] # 지나간 차량
    passing = [] # 지나는 차량
    n = len(truck_weights) # 차량의 수
    passing_time = [0] * n # 차량 별 소요된 시간  
    i = 0
    j = -1
    while len(passed) < n: 
        if len(truck_weights) > 0 and sum(passing) + truck_weights[-1] <= weight:
            passing.append(truck_weights.pop())
            j += 1
        passing_time[:j+1] = [passing_time[z] + 1 for z in range(j+1)] # while문이 돌아갈때마다 1씩 추가 -> 시간이 지나는 것을 표현. 

        if passing_time[i] == bridge_length: # bridge_length와 같게 된다면 그 차량은 지나간 차량임. 따라서 이걸 통해서 passed에 차량을 옮기고 새로운 passing을 만든다. 
            passed.append(passing[0])
            passing = passing[1:]
            i += 1 #지나간 차량 수를 표시한다. 
    return passing_time[0] + 1

print(solution(bridge_length, weight, truck_weights))