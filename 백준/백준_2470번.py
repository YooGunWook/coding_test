n = int(input())
liqur = list(map(int, input().split(" ")))
liqur.sort()


def solution(liqur):
    # 투 포인터 기반 풀이
    left = 0
    right = len(liqur) - 1
    max_mix = liqur[left] + liqur[right]
    fin_left, fin_right = left, right

    while left < right:
        mix = liqur[left] + liqur[right]  # 섞는 과정

        # 계산
        if abs(mix) < abs(max_mix):
            max_mix = mix
            fin_left, fin_right = left, right
            if max_mix == 0:
                break

        # mix가 0보다 크면 right를 줄이고, 반대면 left를 줄인다.
        if mix > 0:
            right -= 1
        else:
            left += 1

    return liqur[fin_left], liqur[fin_right]


print(*solution(liqur))