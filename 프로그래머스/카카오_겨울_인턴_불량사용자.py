import itertools


def solution(user_id, banned_id):
    # 가능한 모든 경우의 수 탐색
    check_list = list(itertools.permutations(user_id, len(banned_id)))
    ans = 0  # 정답
    done_list = []  # 이미 한 케이스는 패스하기 위해 체크
    for check in check_list:
        check = list(check)  # list로 만들어서 체크하기 쉽게 변환
        ban_list = []  # ban 당한 리스트
        for ban in banned_id:
            idx = 0  # id 체크용
            ban_count = ban.count("*")  # * 개수 확인
            while True:
                if len(check) <= idx:  # idx가 check의 길이보다 커지면 없다는 얘기임
                    break
                ck = check[idx]  # 타겟
                if len(ban) != len(ck):  # 길이가 다르면 볼 필요 없음
                    idx += 1
                    continue

                if ban_count == len(ban):  # * 개수가 ban의 길이와 같으면 아무거나 가능
                    ban_list.append(ck)
                    check.remove(ck)
                    break

                res = []  # 길이 체크용
                for tok_idx in range(len(ban)):
                    if ban[tok_idx] == ck[tok_idx]:
                        res.append(ban[tok_idx])

                if len(res) == len(ban) - ban_count:  # 길이가 같으면 밴 리스트
                    ban_list.append(ck)
                    check.remove(ck)
                    break
                else:
                    idx += 1

        if len(banned_id) == len(ban_list):  # ban list일 때
            res = set(ban_list)
            if res not in done_list:  # done_list에 없을때만 업데이트
                done_list.append(res)
                ans += 1
    return ans


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))