import collections


def queensAttack(n, k, r_q, c_q, obstacles):  # 퀸이 공격할 수 있는 위치 count 문제.
    # 시간 제약때문에 살짝 까다로움
    # obstacles를 list에서 dictionary로 바꿈 -> O(n)으로 조회 가능
    dx, dy = [-1, 1, 0, 0, 1, -1, 1, -1], [0, 0, -1, 1, 1, -1, -1, 1]  # 방향
    count = 0  # 정답
    x = r_q - 1  # 위치
    y = c_q - 1  # 위치

    for idx in range(8):  # 모든 방향을 다 조회한다
        nx = x + dx[idx]
        ny = y + dy[idx]
        while (
            0 <= nx < n and 0 <= ny < n and obstacles[(nx + 1, ny + 1)] != 1
        ):  # 이 조건에 맞는다면 계속 탐색
            count += 1
            nx += dx[idx]
            ny += dy[idx]
    return count
