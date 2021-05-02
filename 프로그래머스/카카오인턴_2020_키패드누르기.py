def solution(numbers, hand):
    answer = ""  # 정답
    num_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]  # 키패드 좌표 확인용
    num_dict = {}  # 키패드 좌표 dictionary
    for x in range(4):
        for y in range(3):
            num_dict[num_mat[x][y]] = (x, y)  # 좌표 정보 저장

    left = [1, 4, 7, "*"]  # 왼손 리스트
    right = [3, 6, 9, "#"]  # 오른손 리스트

    # 처음 시작 좌표
    left_thumb = (3, 0)
    right_thumb = (3, 2)

    for num in numbers:  # 각 키패드별로 조회
        if num in left:
            answer += "L"
            left_thumb = num_dict[num]  # 왼손 좌표 업데이트

        elif num in right:
            answer += "R"
            right_thumb = num_dict[num]  # 오른손 좌표 업데이트

        else:  # 가운데 키패드일 때
            loc = num_dict[num]
            loc_x, loc_y = loc  # 눌러야되는 키패드의 좌표
            left_x, left_y = left_thumb
            right_x, right_y = right_thumb
            # 왼손, 오른손 키패드별 거리 차이 구하기
            left_dist = abs(left_x - loc_x) + abs(left_y - loc_y)
            right_dist = abs(right_x - loc_x) + abs(right_y - loc_y)
            # 더 짧은 위치 있는 손가락으로 업데이트
            if left_dist < right_dist:
                answer += "L"
                left_thumb = loc
            elif left_dist > right_dist:
                answer += "R"
                right_thumb = loc
            # 두 손가락의 좌표가 같으면 hand에 따라 손가락 좌표 변경
            elif left_dist == right_dist:
                if hand == "right":
                    answer += "R"
                    right_thumb = loc
                elif hand == "left":
                    answer += "L"
                    left_thumb = loc

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))