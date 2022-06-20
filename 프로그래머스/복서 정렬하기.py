def solution(weights, head2head):
    answer = []  # 정답 체크용

    # 각 선수별로 전적 조회
    for person in range(len(weights)):

        # 초기값 설정
        win_count = 0
        loss_count = 0
        heavy_win = 0
        match_res = head2head[person]

        # 전적 조회
        for other in range(len(match_res)):
            if person == other:  # 같은 사람일 때
                continue
            if match_res[other] == "W":  # 이겼을 때
                win_count += 1

                # 자신보다 무거운 사람을 이겼을 때
                if weights[other] > weights[person]:
                    heavy_win += 1

            # 졌을 때
            elif match_res[other] == "L":
                loss_count += 1

        # 한번도 못 이겼을 때
        if win_count == 0:
            win_ratio = 0
        else:  # 한번이라도 이겼을 때
            win_ratio = win_count / (loss_count + win_count)

        # 전적 넣기
        answer.append((person + 1, win_ratio, heavy_win, weights[person]))

    # 조건에 맞게 sorting
    answer = sorted(answer, key=lambda x: (x[1], x[2], x[3]), reverse=True)
    answer = [ans[0] for ans in answer]
    return answer


print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))
