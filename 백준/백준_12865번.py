"""
이 문제는 아주 평범한 배낭에 관한 문제이다.
한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 
세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.
준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 
각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 
아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 
준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.
"""

n, k = list(map(int, input().split(" ")))
backpack = []  # [[무게, 가치]]
for _ in range(n):
    bag = list(map(int, input().split(" ")))
    backpack.append(bag)

# DP 배낭 문제로 풀어본다.
def solution(backpack, n, k):
    dp = []
    dp.append([0] * (k + 1))  # 초기 값을 넣어준다.
    for i in range(1, n + 1):  # backpack에 들어있는 개수만큼 진행한다. 1부터 시작하는 이유는 위에서 이미 0으로 채웠음.
        dp.append([])  # 우선 빈 리스트를 넣어준다.
        for c in range(k + 1):  # 최대 용량까지 조회를 진행한다.
            if c == 0:  # 0일때는 의미 없기 때문에 바로 0을 넣어준다.
                dp[i].append(0)
            elif backpack[i - 1][0] <= c:  # 현재 무게가 한도보다 작거나 같으면 업데이트를 한다.
                dp[i].append(
                    max(
                        backpack[i - 1][1] + dp[i - 1][c - backpack[i - 1][0]],
                        dp[i - 1][c],
                    )  # 최대 이익인 것을 선택한다.
                )
            else:
                dp[i].append(dp[i - 1][c])
    return dp[-1][-1]


print(solution(backpack, n, k))
