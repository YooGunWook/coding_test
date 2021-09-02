"""
DP 문제
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.
맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.
"""

import copy

n = int(input())
tri = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    tri.append(row)

print(tri)


def solution(n, tri):
    # DP를 활용해서 최대값을 구한다.
    # 이전 결과를 저장해서 업데이트 하는 방식으로 진행
    new_tri = copy.deepcopy(tri)  # 새로운 삼각형을 기록하기 위해 복사를 한다.
    for row in range(n - 1):
        for idx in range(len(tri[row])):  # 값 두개가 겹치는 경우에는 최대값을 선택하게 해준다.
            tri[row + 1][idx] = max(
                tri[row + 1][idx], new_tri[row + 1][idx] + tri[row][idx]
            )
            tri[row + 1][idx + 1] = max(
                tri[row + 1][idx + 1], new_tri[row + 1][idx + 1] + tri[row][idx]
            )

    return max(tri[-1])


print(solution(n, tri))
