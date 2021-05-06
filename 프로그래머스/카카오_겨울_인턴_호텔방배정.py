import bisect
import collections
import copy

# Only 정확성
def solution(k, room_number):
    rooms = {}  # 방 정보
    answer = []  # 배정 정보
    for i in range(1, k + 1):
        rooms[i] = 0  # 각 방별로 정보를 넣어준다.
    room_num = list(rooms.keys())  # 이진탐색용
    for idx, room in enumerate(room_number):
        if rooms[room] == 0:  # 방에 사람이 없으면 바로 넣어줌
            rooms[room] = 1
            answer.append(room)
        else:  # 아니면 이진 탐색으로 가장 가까운 방에 배정
            while True:
                cand = bisect.bisect_right(room_num, room)  # 오른쪽 기준 탐색
                if rooms[room_num[cand]] == 0:  # 비어있으면 배정
                    rooms[room_num[cand]] = 1
                    answer.append(room_num[cand])
                    break
                room = room_num[cand]  # 다음 방으로 탐색

    return answer


# 정확성 + 효율성
def solution2(k, room_number):
    rooms = collections.defaultdict(int)  # 방 정보 저장 + 방문 기록
    answer = []
    for room in room_number:
        n = room  # 방문 기록으로 만든다.
        visit = [n]  # 방문 기록들
        while n in rooms:  # 각 방별로 조회
            n = rooms[n]  # 새로운 n을 설정
            visit.append(n)  # 이걸 통해 빈 방을 찾을 때까지 조회한다
        answer.append(n)  # 정답 넣기
        for vi in visit:  # 방문 기록을 저장한다.
            rooms[vi] = n + 1  # 다음으로 가야될 방을 이걸로 저장해주는 것!
    return answer


room_number = [1, 3, 4, 1, 3, 1]
k = 10
print(solution2(k, room_number))