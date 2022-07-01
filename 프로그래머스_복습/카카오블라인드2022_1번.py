def solution(id_list, report, k):
    id_dict = {ids: idx for idx, ids in enumerate(id_list)}
    answer = [0] * len(id_list)
    id_count = {ids: [] for ids in id_list}
    for r in report:
        r = r.split(" ")
        if r[0] in id_count[r[1]]:
            continue
        id_count[r[1]].append(r[0])
    for i in id_count:
        if len(id_count[i]) >= k:
            for j in id_count[i]:
                answer[id_dict[j]] += 1
    return answer


if __name__ == "__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    k = 2
    print(solution(id_list, report, k))
