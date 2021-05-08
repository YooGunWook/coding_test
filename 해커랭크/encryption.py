import math


def encryption(s):  # 새로 정렬로 된 문장 추출
    l = len(s)  # 문장의 길이
    # lower(sqrt(l)) <= row <= col <= upper(sqrt(l))
    f = math.floor(math.sqrt(l))  # row에 들어갈 케이스
    c = math.ceil(math.sqrt(l))  # col에 들어갈 케이스
    if f * c < l:  # f*c가 l보다 작으면 f를 c로 바꿔준다
        f = c
    mat = []  # 문장 배열 만들기
    row = []  # 한 문장의 list
    for idx, char in enumerate(s):
        row.append(char)
        if len(row) == c:  # 열의 기준에 충족할 때
            mat.append(row)
            row = []
            continue
        if idx == len(s) - 1:  # 충족하지 못한 케이스
            if len(row) < c:
                row += ["0"] * (c - len(row))
                mat.append(row)
    res_mat = []  # 최종 결과 넣는 리스트
    for i in range(c):
        sent = ""  # 새로로 읽을 때 결과
        for j in range(f):
            if mat[j][i] == "0":  # 0이면 비어있는 칸
                continue
            sent += mat[j][i]
        res_mat.append(sent)
    return " ".join(res_mat)  # 최종 결과 반환


print(encryption("chillout"))
