"""
암흑가의 권력은 주먹과 정보에서 나온다. 주먹은 한 명에게 강하고, 정보는 세계를 가지고 놀 수 있기 때문에 호석이는 세상 모든 정보를 모으는 "정보 상인"이 되고 싶다.
정보 상인은 정보를 사고파는 사람을 의미한다.
호석이는 아직 상인계의 새싹이기 때문에, 초기 투자를 통해서 여러 명의 "정보 고릴라"들로부터 정보를 모으려고 한다. 
정보 고릴라란 여기저기서 정보를 수집하는 사람들을 의미한다. 일단 정보를 긁어모으기 위해서 호석이는 여러 정보 고릴라들에게 정보를 구매하려고 한다.
... 이하 생략...
견제를 위해서 호석이가 가진 정보들의 가치 총합, 즉 호석이가 정보들을 구매하는 데에 쓴 돈의 총합을 구하자.
"""
import heapq
import collections

n = int(input())
info_dict = collections.defaultdict(list)  # 고릴라 정보원들이 가지고 있는 정보 리스트
valSum = 0  # 정보 가치 총합

for _ in range(n):

    info = list(map(str, input().split(" ")))

    if info[0] == "1":  # 고릴라 정보
        for val in info[3:]:
            heapq.heappush(info_dict[info[1]], -int(val))  # 최대 힙 활용

    if info[0] == "2":  # 호석이가 사는 정보

        if info[1] not in info_dict:  # 정보 고릴라가 없을 때
            continue
        for _ in range(int(info[2])):  # 산 개수만큼 최대 가치 정보 사기
            if not info_dict[info[1]]:  # 아이템이 비어있을 때
                break
            valSum += -heapq.heappop(info_dict[info[1]])  # 최대 힙이기 때문에 -로 원래대로 변환

print(valSum)
