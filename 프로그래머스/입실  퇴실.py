import collections


def solution(enter, leave):
    room_info = []  # 방안에 있는 사람 정보
    person_info = {i: 0 for i in enter}  # 만난 횟수 체크

    # deque로 변경
    enter = collections.deque(enter)
    leave = collections.deque(leave)

    # 정답 체크 용
    answer = [0] * len(enter)

    # 들어가는 사람이 없을 때 까지
    while enter:
        # 제일 먼저 나가는 사람이 방 안에 있을 때
        if leave[0] in room_info:
            l_person = leave.popleft()
            room_info.remove(l_person)
            continue

        # 방에 사람 들어감
        person = enter.popleft()
        if not room_info:  # 방안에 아무도 없을 때
            room_info.append(person)
            continue

        elif room_info:  # 방안에 한명이라도 있을 때
            # 서로 만나게 됨
            person_info[person] += len(room_info)
            for r_person in room_info:
                person_info[r_person] += 1
            room_info.append(person)

    # 사람 수 세기
    for person in person_info:
        answer[person - 1] = person_info[person]

    return answer


enter = [1, 4, 2, 3]
leave = [2, 1, 3, 4]
print(solution(enter, leave))