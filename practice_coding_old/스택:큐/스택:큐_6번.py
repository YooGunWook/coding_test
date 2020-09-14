prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = [] 
    for i in range(len(prices)-1): # 마지막은 어차피 0이기 때문에 마지막 부분 빼고 계산
        count = 0
        for j in range(i+1,len(prices)): # i+1번째만큼 for문을 돌리고 계산해줘야함. 
            if prices[i] <= prices[j]:  # 가격이 떨어지지 않으면 1을 더해준다.
                count += 1 
            elif prices[i] > prices[j]: # 가격이 떨어진다면 떨어진 1초는 동안은 떨어지지 않았기 때문에 1초 더해주고 그 후는 break로 끝내준다.
                count += 1
                break
        answer.append(count)
    answer.append(0)
    return answer

print(solution(prices))