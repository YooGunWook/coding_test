n = int(input())
stair = [0]  # 가장 처음은 무조건 0
for _ in range(n):
    # 계단 순서대로 점수 추가
    stair.append(int(input()))

# n == 1이면 다른건 굳이 조회할 필요 없음
if n == 1:
    print(stair[1])
else:
    # dp 생성 -> 해당 위치까지 갈 때 최댓값을 넣어준다.
    dp = [0] * (n + 1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    # for문을 통해 최대 값 찾기.
    # 자신의 위치 점수 + 1칸 밑 점수 + 3칸 밑 까지 올라오는 최대 점수와
    # 자신의 위치 점수 + 2칸 밑 점수 중 최대를 선택
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])
    print(dp[n])
