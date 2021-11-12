"""
영선이는 매우 기쁘기 때문에, 효빈이에게 스마일 이모티콘을 S개 보내려고 한다.
영선이는 이미 화면에 이모티콘 1개를 입력했다.
이제, 다음과 같은 3가지 연산만 사용해서 이모티콘을 S개 만들어 보려고 한다.
1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
3. 화면에 있는 이모티콘 중 하나를 삭제한다.
모든 연산은 1초가 걸린다. 또, 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다. 
클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다. 
또한, 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없다. 
화면에 이모티콘을 붙여넣기 하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가된다.
영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.
"""
import collections


S = int(input())


def solution(S):
    # DP + BFS 기반 풀이
    dp = [[-1] * 1001 for _ in range(1001)]
    dp[1][0] = 0
    queue = collections.deque([[1, 0]])
    while queue:
        s, c = queue.popleft()

        # 클립보드에 붙이는 케이스
        if s <= 1000 and dp[s][s] == -1:
            dp[s][s] = dp[s][c] + 1
            queue.append([s, s])

        # 화면에 붙이는 케이스
        if s + c <= 1000 and dp[s + c][c] == -1:
            dp[s + c][c] = dp[s][c] + 1
            queue.append([s + c, c])

        # 화면에 있는 이모티콘을 지우는 케이스
        if s - 1 >= 0 and dp[s - 1][c] == -1:
            dp[s - 1][c] = dp[s][c] + 1
            queue.append([s - 1, c])

        if S == s:
            break

    ans = 1e9
    for i in dp[S]:
        if i != -1:
            ans = min(ans, i)
    return ans


print(solution(S))
