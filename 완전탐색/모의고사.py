def solution(answers):
    answer = {}
    pick_answer = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    picker = 1
    for pick in pick_answer:
        count = 0
        order = 0
        count_same = 0

        while count < len(answers):
            if pick[order] == answers[count]:
                count += 1
                order += 1
                count_same += 1
            else:
                order += 1
                count += 1

            if order + 1 == len(pick) + 1:
                order = 0

            if count == len(answers):
                answer.update({picker: count_same})
                picker += 1
                break

    max_value = max([m for m in answer.values()])
    answer_real = []

    for key, value in answer.items():
        if value == max_value:
            answer_real.append(key)

    return answer_real
