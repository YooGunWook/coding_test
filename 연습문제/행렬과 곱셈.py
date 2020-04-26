def solution(arr1, arr2):
    answer = []
    for i in range(0,len(arr1)):
        # 행렬로 만들어주기 위해 곱한 결과 list를 만들어준다.
        product = []
        # 행을 고정하고 열을 움직이는 형태이기 때문에 
        for j in range(0,len(arr2[0])):
            add = 0
            # 열이 바뀌는 형태이기 때문에 arr[i]의 길이를 loop 돌려준다. 
            for k in range(0,len(arr1[i])):
                a = arr1[i][k] * arr2[k][j]
                # 곱한 값을 add에 중첩해준다.
                add += a
            # 최종 값을 product에 넣어준다.
            product.append(add)
        # product가 된 값을 answer에 넣어준다. 
        answer.append(product)
    return answer

# list(zip(*arr2)) 