n = int(input())
works = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    works.append(row)
# 가장 빨리 끝내야되는 것들을 우선으로 진행해야함
works.sort(key=lambda x: x[1])


def solution(works, n):
    max_time = 0  # 출력값
    for tmp_time in range(0, 1000000):  # 24시간이라 했지만 범위가 1000000임
        done = 0  # 끝난 일 개수
        start_time = tmp_time  # 시작 시간이 계속 바뀌기 때문에 업데이트
        for work in works:
            end_time = start_time + work[0]  # 끝나는 시간 체크
            if end_time <= work[1]:
                start_time = end_time
                done += 1  # 만약 원하는 시간 안으로 끝나면 1 더해준다.
        if done != n and tmp_time == 0:  # 0시부터 모든 일을 끝낼 수 없으면 다른 시간에도 끝내지 못함
            return -1
        if done == n:  # 다 끝내면 max_time 업데이트
            max_time = tmp_time
        elif done != n:  # 언젠가 끝낼 수 없는 시간이 생김. 그땐 max_time 출력
            return max_time


print(solution(works, n))