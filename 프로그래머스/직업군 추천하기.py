def solution(table, languages, preference):
    score_info = {}  # 각 직무 별로 선호 점수
    for job_info in table:
        job_info = job_info.split(" ")
        score_info[job_info[0]] = {}
        score = 5
        for lan in job_info[1:]:
            score_info[job_info[0]][lan] = score
            score -= 1

    # 개발자의 선호 언어
    developer_score = {languages[i]: preference[i] for i in range(len(languages))}

    ans_dict = []  # 정답을 담는 리스트
    for job in score_info:
        score = 0
        for d_lan in developer_score:
            if d_lan not in score_info[job]:
                continue
            score += developer_score[d_lan] * score_info[job][d_lan]  # 최종 점수
        ans_dict.append([job, score])

    ans_dict = sorted(ans_dict, key=lambda x: x[1], reverse=True)  # 점수 순으로 sort
    max_score = ans_dict[0][1]
    chk = []  # 동일 점수가 있을 경우 체크
    for ans in ans_dict:
        if ans[1] == max_score:
            chk.append(ans)
    ans_dict[: len(chk)] = sorted(chk, key=lambda x: x[0])

    return ans_dict[0][0]


table = [
    "SI JAVA JAVASCRIPT SQL PYTHON C#",
    "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
    "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
    "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
    "GAME C++ C# JAVASCRIPT C JAVA",
]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]

print(sorted(["SI", "PORTAL"]))
print(solution(table, languages, preference))