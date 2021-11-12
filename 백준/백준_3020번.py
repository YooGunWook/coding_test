"""
개똥벌레 한 마리가 장애물(석순과 종유석)로 가득찬 동굴에 들어갔다. 
동굴의 길이는 N미터이고, 높이는 H미터이다.
(N은 짝수) 첫 번째 장애물은 항상 석순이고, 그 다음에는 종유석과 석순이 번갈아가면서 등장한다.
아래 그림은 길이가 14미터이고 높이가 5미터인 동굴이다. (예제 그림)
이 개똥벌레는 장애물을 피하지 않는다.
자신이 지나갈 구간을 정한 다음 일직선으로 지나가면서 만나는 모든 장애물을 파괴한다.
위의 그림에서 4번째 구간으로 개똥벌레가 날아간다면 파괴해야하는 장애물의 수는 총 여덟개이다. 
(4번째 구간은 길이가 3인 석순과 길이가 4인 석순의 중간지점을 말한다)
하지만, 첫 번째 구간이나 다섯 번째 구간으로 날아간다면 개똥벌레는 장애물 일곱개만 파괴하면 된다.
동굴의 크기와 높이, 모든 장애물의 크기가 주어진다.
이때, 개똥벌레가 파괴해야하는 장애물의 최솟값과 그러한 구간이 총 몇 개 있는지 구하는 프로그램을 작성하시오.
"""

from bisect import bisect_right

n, h = list(map(int, input().split(" ")))
up = []
down = []
# 위에서 나는 것과 아래에서 나는 것을 구분한다.
for _ in range(n):
    if _ % 2 == 0:
        down.append(int(input()))
    else:
        up.append(int(input()))
up.sort()
down.sort()

# 이분 탐색을 기반으로 정답을 찾는다.
def solution(up, down, n, h):
    ans = n
    cnt = 0
    for i in range(1, h + 1):  # 각 높이별로 조회한다.
        # 개수 찾기
        down_res = len(down) - bisect_right(down, i - 1)  # 원래 높이대로 찾기
        up_res = len(up) - bisect_right(up, h - i)  # 반대로 찾기
        cur_num = down_res + up_res  # 뚫는 개수
        if cur_num < ans:  # 개수보다 작을 때 업데이트
            ans = cur_num
            cnt = 1
        elif cur_num == ans:  # 만약 같으면 1을 더해준다.
            cnt += 1
    return ans, cnt


print(*solution(up, down, n, h))
