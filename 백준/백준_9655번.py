"""
돌 게임은 두 명이서 즐기는 재밌는 게임이다.
탁자 위에 돌 N개가 있다. 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며, 돌은 1개 또는 3개 가져갈 수 있다.
마지막 돌을 가져가는 사람이 게임을 이기게 된다.
두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 작성하시오. 게임은 상근이가 먼저 시작한다.
"""
n = int(input())

# 순서를 정해주는 함수
def changer(phase):
    if not phase:  # 처음은 무조건 SK
        return "SK"
    elif phase == "SK":  # 그다음은 다음 순서에 따라 계속 바뀜
        return "CY"
    elif phase == "CY":
        return "SK"


# dp 기반 풀이
def solution(n):
    phase = ""
    while n >= 0:  # 0이 아닐때까지 계속 탐색 진행
        if n % 3 == 0:  # 이렇게 되면 3개씩만 가져가면 됨.
            cnt = n // 3
            for _ in range(cnt):  # 개수만큼 순서를 바꿔본다
                phase = changer(phase)
            break
        n -= 1  # 3으로 나눠질때까지 1을 빼준다.
        phase = changer(phase)
    return phase


for i in range(1, 100):
    print(i, solution(i))
