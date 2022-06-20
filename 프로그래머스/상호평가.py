def solution(scores):
    answer = ""
    score_dict = {i: [] for i in range(len(scores))}

    for score in scores:
        for idx, s in enumerate(score):
            score_dict[idx].append(s)

    for idx, student in enumerate(score_dict):
        score = score_dict[student]
        max_score = max(score)
        min_score = min(score)
        if (score.count(max_score) == 1 and score[idx] == max_score) or (
            score.count(min_score) == 1 and score[idx] == min_score
        ):
            del score[idx]

        fin_score = sum(score) / len(score)

        if fin_score >= 90:
            answer += "A"
        elif 80 <= fin_score < 90:
            answer += "B"
        elif 70 <= fin_score < 80:
            answer += "C"
        elif 50 <= fin_score < 70:
            answer += "D"
        else:
            answer += "F"

    return answer


print(
    solution(
        [
            [100, 90, 98, 88, 65],
            [50, 45, 99, 85, 77],
            [47, 88, 95, 80, 67],
            [61, 57, 100, 80, 65],
            [24, 90, 94, 75, 65],
        ]
    )
)
