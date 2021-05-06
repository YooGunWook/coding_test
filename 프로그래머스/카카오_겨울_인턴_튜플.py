def solution(s):
    s = s[1:-1].replace(",{", ", {")  # 마지막과 처음에 있는 괄호를 없앤 후 split하기 쉽게 변환
    s = s.split(", ")  # 각 튜플별로 split
    tmp_s = []  # 임시로 s를 담을 리스트
    answer = []  # 정답
    for tup in s:
        tup = tup[1:-1]  # 처음과 끝의 괄호 없애기
        tup = [int(i) for i in tup.split(",")]  # 전부 숫자로 바꿔주기
        tmp_s.append(tup)  # 임시 s에 담는다.
    tmp_s.sort(key=lambda x: len(x))  # 길이 기준으로 sorting
    for tup in tmp_s:  # tup 조회
        for value in tup:  # tup에 있는 숫자 조회
            if value not in answer:  # answer에 없으면 값을 넣어준다.
                answer.append(value)
    return answer


print(solution("{{20,111},{111}}"))