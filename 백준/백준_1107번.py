def solution(N: int, M: int, break_list: list) -> int:

    # 100일 경우 굳이 채널을 옮길 필요 없음
    if N == 100:
        return 0

    # 우선 100에서 부터 시작
    result = abs(N - 100)

    # 0에서부터 하나씩 전부탐색

    for num in range(1000001):
        num_list = list(str(num))
        check_possible = False
        # 누를 수 없는 버튼을 탐색
        for check in num_list:
            if check in break_list:
                check_possible = True
                break

        # 누를 수 없을 경우 굳이 볼 필요 없기 때문에 Pass
        if check_possible:
            continue

        # 탐색한 것과 기존 것 중 그나마 작은 것을 선택
        result = min(result, abs(N - num) + len(str(num)))

    return result