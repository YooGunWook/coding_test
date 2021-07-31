"""
지민이는 항구에서 일한다. 그리고 화물을 배에 실어야 한다. 
모든 화물은 박스에 안에 넣어져 있다. 
항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 
모든 크레인은 동시에 움직인다.

각 크레인은 무게 제한이 있다. 
이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 
모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.
"""

import collections

n = int(input())
crane = list(map(int, input().split(" ")))
m = int(input())
box_weight = list(map(int, input().split(" ")))


def solutio1n(n, crane, m, box_weight):
    time = 0
    crane = sorted(crane, reverse=True)
    # max_crane = max(crane)
    box_weight = sorted(box_weight, reverse=True)
    if box_weight[0] > crane[0]:
        return -1
    count_box = collections.Counter(box_weight)
    box_list = sorted(list(count_box.keys()), reverse=True)

    while True:
        new_box_list = []
        count = 0
        crane_dict = {c: 0 for c in crane}
        if sum(count_box.values()) == 0:
            break

        for box in box_list:
            for c in crane_dict:
                if count_box[box] == 0:
                    break

                if box <= c and crane_dict[c] == 0:
                    crane_dict[c] += 1
                    count_box[box] -= 1
                    count += 1

            if count_box[box] != 0:
                new_box_list.append(box)

        box_list = sorted(new_box_list, reverse=True)

        if count == n:
            time += 1
            continue

        if 0 < count < n:
            time += 1
            continue

        if count == 0:
            break

    return time


#### 검색을 통해 찾은 답안 ####


def solution(n, crane, m, box_weight):

    # 우선 두개의 박스에 대해서 sorting을 진행한다.
    crane.sort(reverse=True)
    box_weight.sort(reverse=True)

    time = 0
    checked = [0 for _ in range(m)]  # 박스 옮겼는지 여부 확인
    count = 0  # 옮긴 박스 개수
    positions = [0] * n  # 각 크레인 별 정보 -> 이걸 통해 박스 정보를 계속 업데이트한다.

    if crane[0] < box_weight[0]:
        return -1

    while count < m:  # 옮긴 박스 개수가 m보다 작을 때 까지 진행
        for i in range(n):  # 크레인별로 확인
            while positions[i] < len(box_weight):
                # 옮기지 않은 박스 중에서 옮길 수 있는 박스를 찾을 때 까지 반복
                if not checked[positions[i]] and crane[i] >= box_weight[positions[i]]:
                    checked[positions[i]] = True
                    positions[i] += 1
                    count += 1
                    break
                positions[i] += 1
        time += 1

    return time


solution(n, crane, m, box_weight)

