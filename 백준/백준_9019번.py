import collections
import sys

n = int(input())

# 명령어에 따라 숫자를 바꿔주는 함수
def transform(t_num, order):
    if order == "D":  # 두배로 바꿔주는 함수
        if t_num * 2 > 9999:  # 기준 값보다 클 때
            return (t_num * 2) % 10000
        else:  # 그 외
            return t_num * 2

    elif order == "S":  # 원래 값에서 1을 빼주는 함수
        if t_num == 0:  # 0일 때는 9999로 바꿔줌
            return 9999
        else:  # 그 외
            return t_num - 1

    elif order == "L":  # 왼쪽으로 회전
        return int((t_num / 1000) + (t_num % 1000 * 10))

    elif order == "R":  # 오른쪽으로 회전
        return int((1000 * (t_num % 10)) + (t_num / 10))


def solution(A, B):
    answer = ""
    order_list = ["D", "S", "L", "R"]  # 명령어 정보
    queue = collections.deque([(A, "")])
    flag = False  # 최솟값 찾기 위한 flag
    visited = [0] * 10000  # 방문 여부 확인
    visited[A] = 1  # 현재값은 이미 방문
    # BFS 실행
    while queue:
        num, orders = queue.popleft()
        for order in order_list:
            new_num = transform(num, order)
            if 0 <= new_num < 10000 and visited[new_num] == 0:
                visited[new_num] = 1
                new_orders = orders + order
                queue.append((new_num, new_orders))
                if new_num == B:
                    answer = new_orders
                    flag = True
                    break

        if flag:
            break

    return answer


for _ in range(n):
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    print(solution(A, B))
