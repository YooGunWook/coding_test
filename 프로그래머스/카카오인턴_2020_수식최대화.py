from itertools import permutations
import copy


def solution(expression):
    exp_list = []  # 수식 안에 있는 기호 확인
    if "-" in expression:
        exp_list.append("-")
        expression = expression.replace(
            "-", " - "
        )  # split을 통해 편리하게 계산하기 위해 기호 앞뒤로 띄어쓰기 추가
    if "+" in expression:
        exp_list.append("+")
        expression = expression.replace(
            "+", " + "
        )  # split을 통해 편리하게 계산하기 위해 기호 앞뒤로 띄어쓰기 추가
    if "*" in expression:
        exp_list.append("*")
        expression = expression.replace(
            "*", " * "
        )  # split을 통해 편리하게 계산하기 위해 기호 앞뒤로 띄어쓰기 추가
    exp_perm = permutations(exp_list, len(exp_list))  # 기호 개수만큼 permutation 만들어주기
    answer = 0
    for exps in exp_perm:  # 각 케이스별로 확인
        tmp_exp = copy.deepcopy(expression)  # 각 케이스별 계산 결과를 확인하기 위해 복사
        for exp in exps:  # 기호별로 확인
            tmp_split = tmp_exp.split(" ")
            idx = 0
            while True:
                tok = tmp_split[idx]
                if tok in exp_list and tok == exp:  # tok이 기호이고 우선순위 기호인지 확인
                    tmp_res = eval(
                        tmp_split[idx - 1] + tmp_split[idx] + tmp_split[idx + 1]
                    )  # 계산해주기
                    tmp = (
                        tmp_split[idx - 1]
                        + " "
                        + tmp_split[idx]
                        + " "
                        + tmp_split[idx + 1]
                    )  # 원래 수식에서 계산 결과로 바꿔줘야함
                    tmp_exp = tmp_exp.replace(tmp, str(tmp_res))
                    tmp_split = tmp_exp.split(" ")  # 바뀐 결과로 split 다시 하기
                    idx = 0
                else:
                    idx += 1  # 기호가 아니면 idx에 1 더해준다.
                if idx == len(tmp_split):  # idx가 split 개수와 같아지면 break
                    break

        tmp_exp = eval(tmp_exp)  # 최종적으로 한번 더 계산
        if answer < abs(int(tmp_exp)):  # 더 큰 케이스일 때만 업데이트
            answer = abs(int(tmp_exp))
    return answer


print(solution("50*6-3*2"))