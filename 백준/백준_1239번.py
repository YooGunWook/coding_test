from itertools import permutations

n = int(input())
num_list = [int(i) for i in input().strip().split(" ")]


def solution(n, num_list):
    # 모든 케이스에 대해서 조회하기 위해 순열 만들기
    cand_chart = permutations(num_list, n)
    max_chart = 0

    # 각 후보별로 탐색
    for chart in cand_chart:
        tmp_chart = chart * 2  # 두개를 붙여서 조회
        cnt = 0

        for i in range(n):
            tmp_sum = 0  # 50일 때 원의 중앙점을 지나게 됨.
            for j in range(i, len(tmp_chart)):
                tmp_sum += tmp_chart[j]  # 50일 때까지 반복
                if tmp_sum == 50:
                    cnt += 1  # 개수 추가
                    break
                elif tmp_sum > 50:  # 50을 넘기면 다음으로 넘어가야함.
                    break
        if max_chart < cnt:  # max_chart보다 크면 새로 갱신
            max_chart = cnt

    return int(max_chart / 2)  # 마지막엔 2로 나눠줘서 진행.


print(solution(n, num_list))
