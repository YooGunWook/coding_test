"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에
가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
"""
n = int(input())
num = list(map(int, input().split(" ")))

# dp 기반 풀이
def solution(n, num):
    dp = [1 for _ in range(n)]  # 각 부분의 시작은 1이기 때문
    for i in range(n):  # i 까지의 증가 여부 확인해야함
        for j in range(i):  # i전까지의 숫자를 기반으로 탐색
            if num[i] > num[j]:  # i가 더 커야 증가하는 거임.
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


print(solution(n, num))
