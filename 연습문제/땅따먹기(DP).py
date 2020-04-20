def solution(land):
    n = len(land)
    # DP를 사용할 것이다. 
    for i in range(0,n-1):
        # 특정 열을 선택하면 특정 열 제외하고 최대값을 찾아준다.
        # 그 후 특정 값과 최댓값이랑 더해준다.
        # n-1번째까지 이 과정을 반복해준다. 
        # 첫째 행은 이 과정이 필요없기 때문에 생략
        # 이렇게하면 최대 값이 나올 수 있다. 
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
    max_value = max(land[n-1])
    return max_value