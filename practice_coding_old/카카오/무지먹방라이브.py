def solution(food_times,k):
    
    # food_items의 합이 k보다 작으면 언제가는 다 0이 되기 때문에 -1로 반환
    if sum(food_times) <= k:
        return -1
    
    # dict로 index:음식 먹는데 걸리는 시간을 만들어준다.
    food_dict = {}
    for i,j in enumerate(food_times):
        food_dict.update({i+1:j})
    
    # value 기준으로 sort를 한다. 
    food_dict = sorted(food_dict.items(), key =(lambda x: x[1]))
    
    # 음식의 개수, 총 걸린 시간, 전에 먹은 음식의 시간, idx를 지정해준다. 
    n = len(food_times)
    sum_k = 0
    previous = 0
    idx = 0
    
    # 먹는데 걸리 총 시간에 ((현재 먹어야 하는 음식 시간 - 전에 먹은 음식 시간) * 음식의 개수)를 더했을 때 k보다 작을 때 까지 반복한다.  
    while sum_k + ((food_dict[idx][1]-previous) * n) < k:
        # 현재 먹어야 되는 음식의 시간
        now = food_dict[idx][1]
        # n번 돌았다는 전제를 깐다. 
        sum_k += (now-previous) * n
        # 다 먹으면 필요 없기 때문에 len를 줄여준다.
        n -= 1
        # 지금 먹은 것의 시간은 이전으로 저장된다.
        previous = now
        # index를 저장해준다. 
        idx += 1
        
    # 다시 원래대로 돌려준다. 대신에 idx부터 시작하는 행렬로 해야된다. 
    result = sorted(food_dict[idx:], key = (lambda x: x[0]))
    
    # k-sum_k = 남은 k의 개수를 현재 남은 음식의 길이로 나눈 값의 나머지가 k번 후 먹어야 되는 음식이다.
    return result[(k-sum_k) % len(result)][0]