import collections
import itertools

"""
창영이는 커피를 좋아한다. 회사에 도착한 창영이는 아침 커피를 즐기려고 한다.
회사에는 N개의 커피가 각각 하나씩 준비되어 있고, 각 커피에는 카페인 함유량 Ci가 있다.
창영이는 N개의 커피 중 몇 개를 골라 정확히 K만큼의 카페인을 섭취하려고 한다.
창영이가 정확히 K만큼의 카페인을 섭취하기 위해서는 최소 몇 개의 커피를 마셔야 할까?
"""
n, k = list(map(int, input().split(" ")))
list_coffee = list(map(int, input().split(" ")))

# 시간 초과
# 모든 경우의 수를 체크하는 것 때문인 듯
def solution(list_coffee, n, k):
    count_coffee = collections.Counter(list_coffee)
    if k in count_coffee:  # 하나만 마셔도 할당량을 채울 수 있는지 여부 확인
        return 1
    for small_n in range(2, n + 1):  # 여러잔을 마셔야 할 때
        cand_coffee = itertools.combinations(list_coffee, small_n)
        for cand in cand_coffee:
            if k == sum(cand):
                return small_n
    return -1


# DP로 해결하는 것이 좋다고 한다.
# 배낭 문제와 매우 비슷하다.
def solution_DP(list_coffee, n, k):

    full_cafe = sum(list_coffee)
    list_coffee = sorted(list_coffee)
    dp = []
    dp.append([0] * (full_cafe + 1))

    for i in range(1, n + 1):
        dp.append([0] * (full_cafe + 1))

        for c in range(1, full_cafe + 1):
            val = dp[i - 1][c - list_coffee[i - 1]]
            if c == list_coffee[i - 1]:
                dp[i][c] = 1
            elif list_coffee[i - 1] < c and val != 0:
                dp[i][c] = val + 1
            else:
                dp[i][c] = dp[i - 1][c]

        for i in dp:
            print(i)
        print()

    if k == 0:
        return 0
    if full_cafe < k or dp[-1][k] == 0:
        return -1
    else:
        return dp[-1][k]


print(solution_DP(list_coffee, n, k))

