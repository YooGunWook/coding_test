def solution(h):
    ans = [0] * len(h) # 우선 탑의 개수만큼 0인 리스트를 만들어준다. 
    for i in range(len(h)-1, 0, -1): # 마지막 탑은 수신할 곳이 없기 때문에 제외하고 for문 돌린다. 
        for j in range(i-1, -1, -1): # i번째보다 높은 탑에서만 송신을 받기 때문에 비교를 해줘야한다. 
            if h[i] < h[j]:
                ans[i] = j+1 # i번째 리스트 값에 수신 탑의 index를 넣어준다. 
                break # break를 통해 for문을 끊어준다. 
    return ans