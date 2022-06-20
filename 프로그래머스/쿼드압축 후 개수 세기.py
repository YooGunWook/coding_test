
# 재귀로 문제 풀기
def comp(x, y, n, arr, ans):
    init = arr[x][y] # 시작점 (이거랑 무조건 같아야함)
    for i in range(x, x + n): # n까지 조회한다. 
        for j in range(y, y + n):
            if arr[i][j] != init: # 같지 않을 경우
                nn = n // 2 # 새로운 사각형 만들기

                # 각 케이스별로 조회한다. 
                comp(x, y, nn, arr, ans) # 범위를 좁히는 경우
                comp(x, y + nn, nn, arr, ans) # y의 범위를 좁히는 경우
                comp(x + nn, y, nn, arr, ans) # x의 범위를 좁히는 경우
                comp(x + nn, y + nn, nn, arr, ans) # 두개 다 줄일 때
                return

    ans[init] += 1


def solution(arr):
    ans = {0: 0, 1: 0} # 정답
    n = len(arr)
    comp(0, 0, n, arr, ans) # 이 안에서 재귀로 실행
    return list(ans.values())


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
